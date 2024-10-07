# GDriveLinkExtractor 🚀

GDriveLinkExtractor is a Python tool that connects to Google Drive 🌐, accesses a specific folder by its folder ID, and fetches all file links (file IDs) within that folder. It leverages the Google Drive API and uses OAuth authentication to securely access the files.

# ✨ Features ✦

🔒 OAuth Authentication: Securely access your Google Drive using OAuth 2.0.

📂 Retrieve File Links: Extract all file IDs from a specified Google Drive folder.

⚡ Efficient and Fast: Quickly access large folders and pull metadata with ease.


# 🛠️ Setup & Installation ✦

1. Create a Google Cloud Project

   First, you need to create a Google Cloud Project to interact with the Google Drive API:
   
   * Go to the Google Cloud Console 🌐 https://console.cloud.google.com
  
   * Click on Create Project to start a new project.

2. Enable the Google Drive API

   * In your project dashboard, navigate to API & Services > Library 📚.
     
   * Search for "Google Drive API" 🔍.
     
   * Click Enable to activate the Google Drive API for your project.

3. Create OAuth Credentials

   * Go to API & Services > Credentials 🛠️.
  
   * Click on Create Credentials and select OAuth Client ID.
  
   * If prompted, configure the OAuth consent screen.
  
   * Choose Desktop app as the application type and create the credentials.
  
   * Download the credentials.json file and place it in your project directory 📂.
  

# 📦 Installation ✦

1. Clone the repository:

   git clone https://github.com/dsprovider/GDrive_Link_Extractor.git

2. Navigate to the project directory:

   cd GDrive_Link_Extractor

3. Install dependencies:

   pip install -r requirements.txt

5. Add your credentials.json file to the root directory.


# 🚀 Usage ✦

1. Run the script
   
2. Authenticate using your Google account when prompted.
   
3. Indicate the folder ID of the Google Drive folder you wish to retrieve file links from.
   
4. The script will output the file links (file IDs) from the folder 📄 to a CSV file.

   Example:
   
   https://drive.google.com/file/d/1abc2def345/view
   
   https://drive.google.com/file/d/6ghi7jkl890/view

🔐 Authentication Details ✦

This project uses OAuth 2.0 to access Google Drive. The first time you run the script, you'll be prompted to authenticate and allow the application to access your Drive. A token will be stored locally to allow future access without re-authentication.

📝 License ✦

This project is licensed under the MIT License.




