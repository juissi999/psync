import os
import hashlib


def find_files_in_folderstructure(folder, files_in_folder):
    folder_contents = os.listdir(folder)
    files = [f for f in folder_contents if os.path.isfile(os.path.join(folder, f))]
    folders = [f for f in folder_contents if not os.path.isfile(os.path.join(folder, f))]

    for f in files:
        # print(os.path.join(folder, f))

        file_with_path = os.path.join(folder, f)

        with open(file_with_path, 'rb') as file_to_check:
            # read contents of the file
            data = file_to_check.read()
            # pipe contents of the file through
            md5_returned = hashlib.md5(data).hexdigest()

        files_in_folder[md5_returned] = file_with_path

    for f in folders:
        find_files_in_folderstructure(os.path.join(folder, f), files_in_folder)
