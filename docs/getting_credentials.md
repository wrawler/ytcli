# Obtaining client_secrets.json from Google Console

### Why We Need client_secrets.json ?

Before we dive into the process, it's essential to understand why we need the `client_secrets.json` file. This file is crucial for authentication and authorization when your application wants to access Google APIs. It contains essential information about your project, including the client ID and client secret, which are used to identify and authenticate your application with Google's API services.

### Steps to Obtain client_secrets.json:

1. **Create a Google Cloud Project**:
   
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - If you're not already signed in, sign in with your Google account.
   - Click on "Select a project" in the upper left corner and choose "New Project."

2. **Name Your Project**:
   
   - Give your project any name you want it doesn't really matter here.
   - Click "Create" to create the project.

3. **Enable APIs and Services**:
   
   - In your project dashboard, click "APIs & Services" on the left sidebar.
   - Click on "Library."

4. **Search for the API**:
   
   - In the library, search for "YouTube Data v3."
   - Click on the API.

5. **Enable the API**:
   
   - Click the "Enable" button to enable the API for your project.

6. **Create OAuth 2.0 Credentials**:
   
   - In the left sidebar, click on "Credentials."
   - Click on "Create Credentials" and select "OAuth client ID."

7. **Configure the OAuth Consent Screen**:
   
   - Choose "Desktop Application" as the application type.
   - Click "Save."

8. **Download client_secrets.json**:
   
   - After configuring the OAuth consent screen, you'll be provided with the option to download the  file.
   - Click "Download" to save the file to your local machine.
   - Save the file named as `client_secret.json`.

9. **Use client_secrets.json in Your Application**:
   
   - Copy the `client_secret.json` file along with `setup.py` file in the directory.

By following these steps, you'll have obtained the `client_secrets.json` file, which is essential for authenticating the application with Google APIs. This file is used to identify your application and ensure secure access to Google services.