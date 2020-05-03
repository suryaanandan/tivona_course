# Questin 3 (part 2)

import os
import zipfile
from os import path


# compresss current working folder using zipfile standard library

path_name = os.getcwd()

print("Compressed folder path : {}".format(path_name))
zip_folder_name = 'Folder_Zipped.zip'
with zipfile.ZipFile(zip_folder_name ,'w', compression = zipfile.ZIP_DEFLATED) as zipping_folder :
    for root, directories, files in os.walk(path_name):
        for cur_file in directories:
            if cur_file == zip_folder_name :
                continue
            try :
                zipping_folder.write(cur_file)
            except FileNotFoundError :
                continue
        for cur_file in files:
            if cur_file == zip_folder_name :
                continue
            try :
                zipping_folder.write(cur_file)
            except FileNotFoundError :
                continue
print("\nFolder compressed\n\n")



# compresss all files in the folder using zipfile standard library
print("Compressed files in path : {}".format(path_name))
zip_folder_name = 'Files_Zipped.zip'
files = []
with zipfile.ZipFile(zip_folder_name ,'w', compression = zipfile.ZIP_DEFLATED) as zipping_files :
    for root, directories, files in os.walk(path_name):
        for cur_file in files:
            if cur_file == zip_folder_name :
                continue
            try :
                    extension = os.path.splitext(cur_file)[-1]
                    if(not(extension == '.zip')) :
                       zipping_files.write(cur_file)
            except FileNotFoundError :
                continue
print("\n Files compression completed")




