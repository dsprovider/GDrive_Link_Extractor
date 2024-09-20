import csv
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

# --------------------------------------------------------------------------------------------------------------------------------

def authenticate_drive():
    """Authenticate the Google Drive API."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('drive', 'v3', credentials=creds)

# --------------------------------------------------------------------------------------------------------------------------------

def list_pdf_files_in_folder(service, folder_id, csv_filename='pdf_files.csv'):
    """Lists all PDF files in the specified Google Drive folder and extracts their IDs, exporting to a CSV file."""
    query = f"'{folder_id}' in parents and mimeType='application/pdf'"
    page_token = None
    files = []

    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['File Name', 'Google Drive File Link'])  # Write header

        while True:
            results = service.files().list(
                q=query,
                spaces='drive',
                fields='nextPageToken, files(id, name)',
                pageToken=page_token,
                pageSize=100
            ).execute()

            items = results.get('files', [])

            if not items:
                print('No PDF files found.')
                break
            else:
                print('PDF Files:')
                for item in items:
                    file_id = item["id"]
                    file_name = item["name"]
                    file_link = f"https://drive.google.com/file/d/{file_id}/view?usp=drive_link"
                    print(f'File Name: {file_name}, File Link: {file_link}')
                    csv_writer.writerow([file_name, file_link])  # Write file details to CSV
                    files.append(item)

            page_token = results.get('nextPageToken', None)
            if page_token is None:
                break

    print(f'>> Details of PDF files exported to {csv_filename}')
    return files  # Return the list of PDF files if needed

# ================================================================================================================================

def main():
    folder_id = '<gdrive_folder_id_here>'
    service = authenticate_drive()
    list_pdf_files_in_folder(service, folder_id)

if __name__ == '__main__':
    main()
