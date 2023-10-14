#!/usr/bin/env python
# __author__ = "Arashdeep Singh"

import json
import os
import argparse
import html
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pytube import YouTube

def load_config():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        return config

    except FileNotFoundError:
        print(f"Configuration file config.json not found.")
        return {}
    
config = None
def initiYtcli():
    with open("config.json","r") as configFile:
        config = json.load(configFile)
        
    api_key = input("Enter your YouTube API key: ")
    download_path = input("Enter custom download path (default = downloads directory in this folder)") or os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_path, exist_ok=True)
    
    config["API_KEY"]               = api_key
    config["DOWNLOAD_PATH"]         = download_path
    config["FIRST_RUN_COMPLETED"]   = "True"
    
    with open('config.json', 'w') as file:
        json.dump(config, file, indent=4)

def searchYoutube(options):
    youtube = build(
        serviceName     =   config.get("API_SERVICE_NAME"),
        version         =   config.get("API_VERSION"),
        developerKey    =   config.get("API_KEY")
    )

    search_response = (
        youtube.search()\
        .list(type=options.mediatype,q=options.search, part="id,snippet", maxResults = options.max_results)\
        .execute()
    )

    results = {}
    resultSrno = 1

    for search_result in search_response.get("items", []):
        if options.mediatype in ["video","channel","playlist"]:
            results[f"{resultSrno}"] = [search_result["id"][f"{options.mediatype}Id"],search_result["snippet"]["title"]]
            resultSrno += 1
        
        else:
            print("Error: Invalid type\n")
            retry = input("\nDo you want to search again (y/n): ")
            if retry == "y":
                searchYoutube(options)
            else:
                print("\nBye :)")

    return results
    
def _selectItem(resultDictionary,Itemtype):
    
    # Printing the serial number and Item name for selecting an option
    for srno,details in resultDictionary.items():
        print(html.unescape(f"{srno}. {details[1]}"))

    selectedID = input(f"\nEnter {Itemtype} serial number: ")

    if selectedID in resultDictionary:
        if Itemtype == "video":
            return "https://www.youtube.com/watch?v="   +  resultDictionary[selectedID][0]

        elif Itemtype == "channel":
            return "https://www.youtube.com/channel/"   +  resultDictionary[selectedID][0]

        elif Itemtype == "playlist":
            return "https://www.youtube.com/playlist?list="    +  resultDictionary[selectedID][0]

    else:
        print("\nError: Enter a valid serial number")
        _selectItem(resultDictionary,Itemtype)

def downloadFromURL(url,mediaType):
    if mediaType == "video":
        streams = YouTube(url).streams.filter(type = mediaType,progressive = True)
        availableResolutions = {}
        streamSrno = 1
        
        print("\nAvailable resolutions:")
        for stream in streams:
            availableResolutions[stream.resolution] = [stream]
            print(f"\n{streamSrno}. {stream.resolution}\t{stream.filesize_mb}MB")
            streamSrno += 1
            
        selectedResolution = input("\nSelect the desired resolution (eg: 720p): ")
        if selectedResolution in availableResolutions:
            availableResolutions[selectedResolution].download()

    elif mediaType == "audio":
        audio = YouTube(url)\
            .streams\
            .get_audio_only()

        audio.download()
    
    else:
        print("\nError: Invalid Option Selected\nKindly re-enter a valid option")
        downloadFromURL(url,mediaType)

def print1():
    print(1)
    
def print2():
    print(2)

def print3():
    print(3)
    
# TODO: convert it into an interactive application
if __name__ == "__main__":
    print("\nWelcome to ytcli, use 'exit' to exit the application\n")
    
    config = load_config()
    if config.get("FIRST_RUN_COMPLETED") == "False":
        initiYtcli()
    
    DEVELOPER_KEY               = config.get("API_KEY")
    YOUTUBE_API_SERVICE_NAME    = config.get("API_SERVICE_NAME")
    YOUTUBE_API_VERSION         = config.get("API_VERSION")
    
    while True:
        user_input = input(">>")
        if user_input == 'exit':
            break

        try:
            exec(user_input)  # Execute the user's input as Python code
            
        except Exception as e:
            print(f"Error: {e}")
    

    
    # parser = argparse.ArgumentParser()
    
    # parser.add_argument(    "--download"    ,   help = "Download media via URL"                                             ,   default = None          )
    # parser.add_argument(    "--mediatype"   ,   help = "Type of media to search (video/audio)"                              ,   default = "video"       )
    # parser.add_argument(    "--searchtype"  ,   help = "Type of Item to search (video/channel/playlists)"                   ,   default = "video"       )
    # parser.add_argument(    "--search"      ,   help = "Search term"                                                        ,   default = "Google"      )
    # parser.add_argument(    "--max-results" ,   help = "Max number of results to display once"                              ,   default = 25            )

    # args = parser.parse_args()

    # try:
    #     if args.download is not None:
    #         downloadFromURL(args.download,args.mediatype)

    #     elif args.search is not None:
    #         result = searchYoutube(args)
    #         selectedItemURL = _selectItem(result,args.mediatype)

    #         if(args.mediatype == "video"):
    #             downloadFromURL(selectedItemURL,args.mediatype)

    #         else:
    #             print(selectedItemURL)

    # except HttpError as e:
    #     print("\nError: An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))