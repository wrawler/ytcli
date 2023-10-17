<img title="" src="https://github.com/wrawler/ytcli/blob/main/logo.png?raw=true" alt="" width="300">

Ytcli is a command-line based application which helps to perform various YouTube requests via command-line

# Requirements

- [Python](https://www.python.org/downloads/) installed on the system (latest version recommended)

- [Pip](https://pip.pypa.io/en/stable/installation/) installed for managing python modules

- [ffmpeg](https://ffmpeg.org/download.html) for muxing audio and video files. 
  
   Also verify installations by running these commands in a terminal:
  
  ```
  python --version
  ```
  
  ```
  pip --version
  ```
  
  ```
  ffmpeg --version
  ```

# How to Install

1. Clone the repository or download the Zip File
   To clone the repository run
   
   ```
   git clone --recursive https://github.com/wrawler/ytcli.git
   ```
   
   Or just download the zip file and extract it

2. Obtain the *client_secret.json* file by creating a project on Google Cloud Console.
   For learning how to do so, see -> [Getting Credentials](docs/getting_credentials.md)

3. Run the setup script
   
   ```
   python setup.py
   ```
   
   The script downloads the required python modules for the project.

4. Enter the desired download path for installation

5. Authenticate via OAuth in the browser.
   
   #### Why is the authentication done:
   
   - **Security:** Authentication ensures that your application is only used by authorized users and that unauthorized access is prevented. It helps protect sensitive user data.
   
   - **User Authorization:** Authentication is also about obtaining the user's consent. Users need to grant permission to your application to access their YouTube data. This is a fundamental aspect of privacy and data protection.
   
   - **Rate Limiting:** Many APIs, including the YouTube API, enforce rate limits to prevent abuse. Authentication helps the API provider identify your application and apply rate limits accordingly.
   
   - **Auditability:** Authentication provides a way to track and audit API usage. This can be important for both you as a developer and the API provider.

6. Decide if executable needs to be created or not during setup.

7. You are good to go !

# Usage

1) Open the terminal in the directory and run following command to enter the interactive terminal.
   
   ```
   python ytcli.py
   ```
   
   or just open the executable present in dist/ytcli directory if you had created the executable.
   
   **NOTE:** You can create a shortcut to this executable anywhere on your system. This would allow usage of this application without having to enter install directory. 

2) Run help to see the available commands along with examples

# Future Goals

- Support of channel info querries
- View videos in a playlist
- Multiple searches with new/next results