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

1. Run the setup script
   
   ```
   python setup.py
   ```
   
   The script downloads the required python modules for the project.

2. Enter the desired download path

3. Authenticate via OAuth in the browser.
   
   #### Why is the authentication done:
   
   - **Security**: Authentication ensures that your application is only used by authorized users and that unauthorized access is prevented. It helps protect sensitive user data.
   
   - **User Authorization**: Authentication is also about obtaining the user's consent. Users need to grant permission to your application to access their YouTube data. This is a fundamental aspect of privacy and data protection.
   
   - **Rate Limiting**: Many APIs, including the YouTube API, enforce rate limits to prevent abuse. Authentication helps the API provider identify your application and apply rate limits accordingly.
   
   - **Auditability**: Authentication provides a way to track and audit API usage. This can be important for both you as a developer and the API provider.
   
   

4. Done! Now you can use the application as you want.