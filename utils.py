import os
import hashlib
import shutil


def find_files_in_folderstructure(folderparts):
    folderpath = os.path.join(*folderparts)

    folder_contents = os.listdir(folderpath)
    files = [f for f in folder_contents if os.path.isfile(os.path.join(folderpath, f))]
    folders = [f for f in folder_contents if not os.path.isfile(os.path.join(folderpath, f))]

    files_found = []

    for filename in files:
        # print(os.path.join(folder, f))

        with open(os.path.join(folderpath, filename), 'rb') as file_to_check:
            # read contents of the file
            data = file_to_check.read()
            # pipe contents of the file through
            md5_of_file = hashlib.md5(data).hexdigest()

        #files_in_folder.append((folder, filename, md5_of_file))
        files_found.append((folderparts, filename, md5_of_file))

    for foldername in folders:
        files_found = files_found + find_files_in_folderstructure(folderparts + [foldername])

    return files_found


def copy_files(files_to_copy, inputdir, outputdir):
    for f in files_to_copy:
        source_folder = os.path.join(*f[0])
        source_file = os.path.join(source_folder, f[1])
        dest_file = os.path.join(outputdir, f[1])
        shutil.copyfile(source_file, dest_file) #, follow_symlinks=False
