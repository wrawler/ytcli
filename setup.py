import subprocess
import json
import os
import shutil
from google_auth_oauthlib.flow import InstalledAppFlow

required_modules = ['argparse', 'google-api-python-client', 'pytube','google_auth_oauthlib','tabulate','pathvalidate','pyinstaller']
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
        
    download_path = input("\nEnter custom download path (default = downloads directory in this folder)") or os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_path, exist_ok=True)
    
    config["DOWNLOAD_PATH"]         = download_path
    config["FIRST_RUN_COMPLETED"]   = "True"
    
    with open('config.json', 'w') as file:
        json.dump(config, file, indent=4)
    
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=["https://www.googleapis.com/auth/youtube.force-ssl"])
    credentials = flow.run_local_server(port=8080)

    with open("credentials.json", "w") as credentials_file:
        credentials_file.write(credentials.to_json())

if __name__ == "__main__":
    install_required_modules()
    config = load_config()
    if config.get("FIRST_RUN_COMPLETED") == "False":
        initiYtcli()
    print("\nConfiguration Completed !!")
    
    binCreate = input("\nDo you want to create executable? (y/n) [default y]: ") or 'y'
    if binCreate == 'y':
        print("Creating executable..\n")
        
        subprocess.check_call(['pyinstaller','ytcli.py'])
        print("\nExecutable created at in directory 'dist'")
        
        credentialsFileDestionation = os.path.join("dist","ytcli", "credentials.json")
        configFileDestionation = os.path.join("dist","ytcli", "config.json")
        
        os.rename("config.json",configFileDestionation)
        os.rename("credentials.json",configFileDestionation)
        
        cleanDir = input("Clean the build files(y/n) [default y]: ") or 'y'
        if cleanDir == 'y':
            shutil.rmtree("build")
            if os.path.exists("__pycache__") and os.path.isdir("__pycache__"):
                shutil.rmtree("__pycache__")
            
        cleanPyScripts = input("Delete the python scripts and keep only the binary(y/n): default y") or 'y'
        if cleanPyScripts == 'y':
            os.remove("multiplex.py")
            os.remove("setup.py")
            os.remove("ytcli.py")
            os.remove("client_secret.json")
            os.remove(".gitignore")