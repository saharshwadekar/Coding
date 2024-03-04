import os
import shutil

path: str = input("Enter $PATH = ")
files = os.listdir(path)

for file in files:
    fileName , fileExtension = os.path.splitext(file)
    extension = fileExtension[1:]
    
    if os.path.exists(path + "/" + extension):
        shutil.move(path + "/" + file, path + "/" + extension + "/" + file)
    else:
        os.makedirs(path + "/" + extension)
        shutil.move(path + "/" + file, path + "/" + extension + "/" + file)
        