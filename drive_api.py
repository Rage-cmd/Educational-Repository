from __future__ import print_function
import io

import os.path
import re
import json 
import mimetypes

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/drive.file',
          'https://www.googleapis.com/auth/drive.appdata']


# Function to get the list of folders based on the query
def search_folder(folder_name = None, folder_id = None, fields = "id, name", verbose = True):
    """
    Returns folder(s) based on the query passed. If two folders are found with the same name, both are returned.
    The query can be passed as a folder name or folder ID. If both are passed, the folder name is ignored. 
    
    Parameters:
        folder_name (str): Name of the folder to search for. If None, the query is based on the folder ID.
        folder_id (str): ID of the folder to search for. Defaults to None.
        fields (str): Fields to return. Example: "files(id, name, parents, webViewLink, owners)". Defaults to "files(id, name, parents, webViewLink, owners)".
        verbose (bool): Prints the results of the search.

    Returns:
        A tuple containing the folder ID(s) and the metadata(the fields argument decides the metata) of the folder(s) as a dictionary.

    Raises:
        Exception: If no folders are found.

    Example::

        f1 = search_folder(folder_id = '1r6JXAFjnmliezL23pf0FePbuJpUJyl-e', fields = "id, name, parents, webViewLink, owners")    
    """
    
    try:
        results = None
        ids = None
        if folder_name:
            fields = "files(" + fields + ")"
            query = "name = '%s' and  mimeType = 'application/vnd.google-apps.folder' and trashed = false" % folder_name
            results = service.files().list(q=query, fields=fields).execute()
            ids = [file.get('id') for file in results.get('files', [])]

        elif folder_id:
            results = service.files().get(fileId=folder_id, fields=fields).execute()
            ids = [results.get('id')]

        else:
            raise Exception("Please specify either folder name or folder ID.")

        # if not items:
        #     print('No files found.')
        #     return
        # print('Files:')
        # for item in items:
        #     print(u'{0} ({1})'.format(item['name'], item['id']))

    except HttpError as error:
        print(f'An error occurred: {error}')
    
    if verbose:
        print(json.dumps(results, indent=4, sort_keys=True))

    return (ids, results)

def remove_folder(folder_id):
    service.files().delete(fileId=folder_id).execute()

def remove_file(file_id):
    service.files().delete(fileId=file_id).execute()


def create_folder(folder_name, parent_folder_id, fields = "id, name"):
    """
    Creates a folder in the parent folder specified. If the parent_folder_id is None, the folder is created in the root folder.

    Parameters:
        folder_name (str): Name of the folder to create.
        parent_folder_id (str): Dictionary containing the details of the created folder.

    Returns:
        The file metadata of the created folder as a dictionary according to the fields argument given.
    """

    file_metadata = {
    'name' : folder_name,
    'mimeType' : 'application/vnd.google-apps.folder'
    }

    if parent_folder_id:
        file_metadata['parents'] = parent_folder_id

    file = service.files().create(body=file_metadata,
                                    fields=fields).execute()

    print("File Response:", file)
    print("\n")
    print ('Folder ID: %s' % file.get('id'))
    return file


def upload_file(file_name, file_path, parent_folder_id, fields = "id, name"):
    """
    Uploads a file to the specified folder. If the parent_folder_id is None, the file is uploaded to the root folder.

    Parameters:
        file_name (str): Name of the file to upload.
        file_path (str): Path (in the local disk) of the file to be uploaded.
        parent_folder_id (str): Parent folder ID in which the file is to be uploaded.

    Returns:
        Dictionary containing the details of the uploaded file.
    
    Raises:
        Exception: If the file is not found.
    """

    # if no extention is given in the name then raise exception
    if not re.search(r'\.[^.]*$', file_name):
        raise Exception("File name must have an extension.")
    
    # if file is not found then raise exception
    if not os.path.isfile(file_path):
        raise Exception("File not found.")

    # get the extension from the file name and set the mime type
    extension = os.path.splitext(file_name)[1]
    mimetype = mimetypes.types_map.get(extension)
    
    # get the file size
    file_size = os.path.getsize(file_path)

    # if file size is greater than 5 MB, use resumable upload
    if file_size > 5242880:
        media = MediaFileUpload(file_path, resumable=True, mimetype=mimetype)
    else:
        media = MediaFileUpload(file_path, mimetype=mimetype)

    file_metadata = {'name': file_name}

    # if parent folder ID is not None, add it to the file metadata
    if parent_folder_id:
        file_metadata['parents'] = parent_folder_id

    # call the Drive v3 API
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields=fields).execute()

    print("File Response:", json.dumps(file, indent=4, sort_keys=True))
    print ('File ID: %s' % file.get('id'))
    return file.get('id')


def download_file(file_id,file_name):
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)


def get_credentials(creds,file_name):
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(file_name, SCOPES)
            creds = flow.run_local_server(port=55167)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return creds



    print("--------------------------")
    # by id 
    f1 = search_folder(folder_id = '1r6JXAFjnmliezL23pf0FePbuJpUJyl-e', fields = "id, name, parents, webViewLink, owners")
    print(f1)

    # f2 = search_folder(folder_id = '1wdvE8Kb6-DgkhueUl6UzRmbPAm5G34E3')
    # print(f2)
    #-------------------------------------------

    #----- Create folder in root directory------
    # create_folder('Networking', None)
    #-------------------------------------------

    #----- Create folder in non-root folder-----
    # f2 = search_folder('Networking')
    # create_folder('Application Layer', [f2])

    # f2 = create_folder('Hoffman Encoding', ['1r6JXAFjnmliezL23pf0FePbuJpUJyl-e'], fields = "id, name, parents, webViewLink, owners")
    # print(f2)
    #-------------------------------------------

    #------------- Upload a file ---------------
    f3 = search_folder('Cyber Security')
    uploaded_file_id = upload_file('big_cat_video.mp4', '/Users/rajeevgoyal/Downloads/videos/big_cat_video.mp4', f3[0])
    #-------------------------------------------

    # f = search_file('limgrave.jpg')
    # print(f.get('id'))
    # download_file(f.get('id'), 'limgrave.jpg')
    # download_file("limgrave.jpg","downloaded_limgrave.jpg")

    # f = search_folder('Security')
    # upload_file('cat_video.mp4', '/Users/rajeevgoyal/Downloads/videos/cat_video.mp4', f)