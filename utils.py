import os
import hashlib


def find_files_in_folderstructure(folder, files_in_folder):
    folder_contents = os.listdir(folder)
    files = [f for f in folder_contents if os.path.isfile(os.path.join(folder, f))]
    folders = [f for f in folder_contents if not os.path.isfile(os.path.join(folder, f))]

    for filename in files:
        # print(os.path.join(folder, f))

        with open(os.path.join(folder, filename), 'rb') as file_to_check:
            # read contents of the file
            data = file_to_check.read()
            # pipe contents of the file through
            md5_of_file = hashlib.md5(data).hexdigest()

        files_in_folder.append((folder, filename, md5_of_file))

    for filename in folders:
        find_files_in_folderstructure(os.path.join(folder, filename), files_in_folder)
