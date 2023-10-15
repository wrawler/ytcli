import subprocess
import json
import os

required_modules = ['argparse', 'googleapiclient', 'pytube']
def install_required_modules():
    for module in required_modules:
        try:
            subprocess.check_call(['pip', 'install', module])
            print(f'Successfully installed {module}')
            
        except subprocess.CalledProcessError:
            print(f'Failed to install {module}')

def load_config():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        return config

    except FileNotFoundError:
        print(f"Configuration file config.json not found.")
        return {}

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

if __name__ == "__main__":
    install_required_modules()
    config = load_config()
    if config.get("FIRST_RUN_COMPLETED") == "False":
        initiYtcli()