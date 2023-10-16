#!/usr/bin/env python

import html
import argparse
from tabulate import tabulate
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from pytube import YouTube
from pathvalidate import sanitize_filename

from setup import load_config
from multiplex import combineAudioVideo

credentials = Credentials.from_authorized_user_file("credentials.json")
config = load_config()
def searchYoutube(searchTerm,searchType,maxResults):
    youtube = build(
        serviceName     =   config.get("API_SERVICE_NAME"),
        version         =   config.get("API_VERSION"),
        credentials     =   credentials
    )

    search_response = (
        youtube.search()\
        .list(type=searchType,q=searchTerm, part="id,snippet", maxResults = maxResults)\
        .execute()
    )

    resultSrno = 1
    for search_result in search_response.get("items", []):
        if searchType in ["video","channel","playlist"]:
            if searchType == "video":
                videoID = search_result["id"]["videoId"]
                videoTitle = search_result["snippet"]["title"]
                videoURL = "https://www.youtube.com/watch?v=" + videoID
                print((f"\n{resultSrno}. {html.unescape(videoTitle)}\n\tURL: {videoURL}"))
            
            elif searchType == "channel":
                channelID = search_result["id"]["channelId"]
                channelTitle = search_result["snippet"]["title"]
                channelURL = "https://www.youtube.com/channel/" + channelID
                print((f"\n{resultSrno}. {html.unescape(channelTitle)}\n\tURL: {channelURL}"))
            
            elif searchType == "playlist":
                playlistID = search_result["id"]["playlistId"]
                playlistTitle = search_result["snippet"]["title"]
                playlistURL = "https://www.youtube.com/playlist?list=" + playlistID
                print((f"\n{resultSrno}. {html.unescape(playlistTitle)}\n\tURL: {playlistURL}"))
            resultSrno += 1

        else:
            print("Error: Invalid type\n")

def downloadFromURL(url,mediaType):
    if mediaType == "video":
        streams = YouTube(url).streams
        videostreams = streams.filter(file_extension="webm",type = mediaType,only_video="True").order_by("resolution").desc()
        
        videoData = []
        highest_fps_by_resolution = {}

        for stream in videostreams:
            if (stream.resolution not in highest_fps_by_resolution) or (stream.fps > highest_fps_by_resolution[stream.resolution][1] and stream.resolution in highest_fps_by_resolution):
                highest_fps_by_resolution[stream.resolution] = (stream.itag , stream.filesize_mb)

        for resolution,details in highest_fps_by_resolution.items():
            itag, filesize = details
            videoData.append([itag,resolution,filesize])
            
        print(tabulate(videoData, headers = ["Itag", "Resolution", "Filesize (MB)"], tablefmt="fancy_grid"))
        
        selectedItag = input("\nSelect the video ID (eg: 17): ")
        video = streams.get_by_itag(selectedItag)
        audio = streams.get_audio_only()
        
        videoTitle = sanitize_filename(YouTube(url).title)
        video.download(output_path = "temp/",filename="temp.webm")
        audio.download(output_path = "temp/",filename="temp.mp4")
        
        combineAudioVideo(videoTitle)
         
        print(f'\nFile Downloaded to {config.get("DOWNLOAD_PATH")}/{mediaType}s')

    elif mediaType == "audio":
        audio = YouTube(url)\
            .streams\
            .get_audio_only()

        audio.download(output_path = f'{config.get("DOWNLOAD_PATH")}/audios')

    else:
        print("\nError: Invalid Option Selected\nKindly re-enter a valid option")

def handleUserInput(user_input):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='action',title='actions')
    
    # Subparser for 'search' action
    search_parser = subparsers.add_parser('search', help="Search YouTube")
    search_parser.add_argument('--term',        default = 'hello',  help="Search term")
    search_parser.add_argument('--searchtype',  default = 'video',  help="Type of item to search (video/channel/playlists)")
    search_parser.add_argument('--maxresults',  default = 25,       help="Max number of search results",    type=int)
    
    # Subparser for 'download' action
    download_parser = subparsers.add_parser('download', help="Download media from URL")
    download_parser.add_argument('--url',       help="URL to download")
    download_parser.add_argument('--mediatype', help="Type of media to download (video/audio)",     default='video')
    
    help_parser = subparsers.add_parser('help')
    
    parts = user_input.split()
    args = parser.parse_args(parts)

    if args.action == 'search':
        searchYoutube(args.term,args.searchtype,args.maxresults)
        
    elif args.action == 'download':
        downloadFromURL(args.url, args.mediatype)
    
    elif args.action == 'help':
        pass
        
    else:
        print("Invalid command. Available commands: 'search' or 'download'")

if __name__ == "__main__":
    print("\nWelcome to ytcli, use 'exit' to exit the application\n")
    
    while True:
        user_input = input(">> ").strip()

        if user_input == 'exit':
            break

        try:
            handleUserInput(user_input)

        except HttpError as e:
            print("\nError: An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
            
        except Exception as err:
            print(f"Error: {err}")