# Questin 3 (part 1)

import os
import tarfile
from os import path

# file path
path_name = os.getcwd()

# compresss current working folder using zipfile standard library

print("Compressed folder path : {}".format(path_name))
tar_folder_name = 'Folder_tar.tar.gz'
with tarfile.open(tar_folder_name, 'w:gz') as tar_folder :
    for root, directories, files in os.walk(path_name):
        for cur_file in directories :
            tar_folder.add(cur_file)
            if cur_file == tar_folder_name :
                continue
            try :
                tar_folder.add(cur_file)
            except FileNotFoundError :
                continue
        for cur_file in files :
            if(cur_file == tar_folder_name) :
                continue
            try :
                tar_folder.add(cur_file)
            except FileNotFoundError :
                continue

print("\nFolder compressed using tarfile standard library\n\n")



# compresss all files in the folder using tarfile standard library
print("Compressed files in path : {}".format(path_name))
zip_folder_name = 'Files_tar.tar.gz'
Allfiles = []
with tarfile.open(zip_folder_name ,'w:gz') as tar_handle :
    for root, directories, files in os.walk(path_name):
        for cur_file in files :
            if cur_file == zip_folder_name :
                continue
            try :
                extension = os.path.splitext(cur_file)[-1]
                if(not((extension == '.zip') or (extension == '.gz'))) :             
                    tar_handle.add(cur_file)
            except FileNotFoundError :
                continue
print("\n Files compression completed using tarfile standard library")







