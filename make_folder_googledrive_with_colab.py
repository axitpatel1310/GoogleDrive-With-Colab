# -*- coding: utf-8 -*-
"""Make-Folder-GoogleDrive-With-Colab.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LcyKDD59lgmwRVOTIg2hfQreNDYG94-s
"""

!pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# Authenticate and create the service
auth.authenticate_user()
from google.auth import default
creds, _ = default()

drive_service = build('drive', 'v3', credentials=creds)

def create_folder(folder_name, parent_id=None):
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    if parent_id:
        file_metadata['parents'] = [parent_id]

    file = drive_service.files().create(body=file_metadata, fields='id').execute()
    folder_id = file.get('id')
    print(f'Folder "{folder_name}" created with ID: {folder_id}')
    return folder_id

folder_id = create_folder('MyNewFolder')