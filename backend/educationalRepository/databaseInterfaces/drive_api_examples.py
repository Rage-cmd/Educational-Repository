import drive_api as drive

creds = drive.get_credentials('credentials.json')
service = drive.build('drive', 'v3', credentials=creds)

#----------- Search for folder ------------
# by name
ids, fields = drive.search_folder(folder_name = 'Application Layer')

# by id 
ids, fields = drive.search_folder(folder_id = '1r6JXAFjnmliezL23pf0FePbuJpUJyl-e', fields = "id, name, parents, webViewLink, owners")


#----- Create folder in root directory------
folder_metadata = drive.create_folder('Networking', None, fields = "id, name, parents, webViewLink, owners")


#----- Create folder in non-root folder-----
ids, fields = drive.search_folder('Networking')
folder_metatdata = drive.create_folder('Application Layer', [ids])

folder_metadata = drive.create_folder('Hoffman Encoding', ['1r6JXAFjnmliezL23pf0FePbuJpUJyl-e'], fields = "id, name, parents, owners")
print(folder_metadata)


#------------- Upload a file ---------------
ids, fields = drive.search_folder('Cyber Security')
uploaded_file_id = drive.upload_file('big_cat_video.mp4', '/Users/rajeevgoyal/Downloads/videos/big_cat_video.mp4', ids[0])


#------------- Download a file -------------
ids, fields = drive.search_file('limgrave.jpg')
drive.download_file(ids[0], 'drive_limgrave.jpg', '/Users/rajeevgoyal/Downloads/images/')

#-------------- Remove a file --------------
ids, fields = drive.search_folder('Cyber Security')
drive.remove_folder(ids[0])
