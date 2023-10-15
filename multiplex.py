import subprocess
import os
from setup import load_config

def combineAudioVideo(videoTitle):
    config = load_config()
    outputPath = f'{config.get("DOWNLOAD_PATH")}/videos'

    ffmpeg_command = [
        "ffmpeg",
        "-i", f"temp/temp.webm",   # Video, audio file and combined file have name same as video title
        "-i", f"temp/temp.mp4",
        "-c:v", "copy",
        "-c:a", "copy",
        f"{outputPath}/{videoTitle}.mp4"
    ]
    
    try:
        subprocess.run(ffmpeg_command, check=True)
        os.remove("temp/temp.webm")
        os.remove("temp/temp.mp4")
        
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")