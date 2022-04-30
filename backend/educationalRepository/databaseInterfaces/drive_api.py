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
    """
    Removes the folder specified.

    Parameters:
        folder_id (str): ID of the folder to be removed.
    
    Returns:
        None
    
    Raises:
        Exception: If the folder is not found.
    """
    service.files().delete(fileId=folder_id).execute()


def remove_file(file_id):
    """
    Removes the file specified.

    Parameters:
        file_id (str): ID of the file to be removed.
    
    Returns:
        None
    
    Raises:
        Exception: If the file is not found.
    """
    service.files().delete(fileId=file_id).execute()


def create_folder(folder_name, parent_folder_id, fields = "id, name"):
    """
    Creates a folder in the parent folder specified. If the parent_folder_id is None, the folder is created in the root folder.

    Parameters:
        folder_name (str): Name of the folder to create.
        parent_folder_id (str): List containing the IDs of the parent folder.

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
        parent_folder_id (List): List of the parent folder ID in which the file is to be uploaded.

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
    return file


def download_file(file_id, file_name, file_path = "./"):
    """
    Downloads a file from the Google Drive using the file ID.

    Parameters:
        file_id (str): File ID of the file to be downloaded.
        file_name (str): Name of the file to be downloaded.
        file_path (str): Path (in the local disk) to store the downloaded file. The default is the current directory.

    Returns:
        None
    
    Raises:
        Exception: If the file is not found.
    """

    # Call the Drive v3 API with the file ID
    request = service.files().get_media(fileId=file_id)

    # Create a file in the current directory to store the downloaded file
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)

    # Download the file in chunks and write to the current directory

    try:
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print ("Download %d%%." % int(status.progress() * 100))
        with io.open(file_path + file_name, 'wb') as f:
            fh.seek(0)
            f.write(fh.read())
        print ("File Downloaded!")

    except HttpError as error:
        print(f'Cannot Download. An error occurred: {error}')


def get_credentials(file_name):
    """
    Gets valid user credentials from storage. If nothing has been stored, or if the stored credentials are invalid, the OAuth2 flow 
    is completed to obtain the new credentials. 

    Parameters:
        file_name (str): Name of the file containing the client secret.

    Returns:
        Credentials, the obtained credential.
    
    Raises:
        Exception: If the credentials are not valid.
    """

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    creds = None

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


def search_file(file_name = None, file_id = None, fields = "id, name", verbose = "False"):
    """
    Searches for a file in the Google Drive using the file name or file ID. If the file is found, the file ID is returned. 

    Parameters:
        file_name (str): Name of the file to be searched. Default is None.
        file_id (str): File ID of the file to be searched. Default is None.
        fields (str): Fields to be returned. Default is "id, name".
        verbose (str): If True, prints the response. Default is False.

    Returns:
        A tuple containing the file ID and the fields queried.
    
    Raises:
        Exception: If the file is not found.
    """

    try:
        results = None
        ids = None
        # Call the Drive v3 API
        if file_name:
            fields = "files(" + fields + ")"
            query = "name = '%s' and mimeType != 'application/vnd.google-apps.folder' and trashed = false" % file_name,
            results = service.files().list(q = query, fields=fields).execute()
            ids = [item['id'] for item in results.get('files', [])]

        elif file_id:
            results = service.files().get(fileId = file_id, fields=fields).execute()
            ids = [results['id']]

        else:
            raise Exception("Please specify either file name or file ID.")

    except HttpError as error:
        print(f'Cannot Search. An error occurred: {error}')
    
    if verbose:
        print(json.dumps(results, indent=4, sort_keys=True))

    return (ids, results)

# if __name__ == '__main__':
    
creds = get_credentials('/Users/rajeevgoyal/Academics/Sem 8/Educational Repository/OAuth keys/credentials.json')
service = build('drive', 'v3', credentials=creds)
