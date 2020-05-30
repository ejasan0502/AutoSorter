import tkinter
from tkinter import filedialog
import os
from os import path
import shutil
from tqdm import tqdm

imageFormats = ['.jpg', '.jpeg', '.gif', '.png', '.tif']
appFormats = ['.exe', '.msi', '.zip', '.rar', '.iso']
audioFormats = ['.wav', '.mp3']
modelFormats = ['.fbx', '.obj']
docFormats = ['.pdf', '.docx', '.txt', '.ods', '.xls']
videoFormats = ['.mkv', '.avi', '.mp4']
categories = ['Images', 'Applications', 'Audio', 'Models', 'Documents', 'Videos', 'Folders', 'Other']

root = tkinter.Tk()
root.withdraw()
root = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a folder to autosort')

def CreateFolders():
    for category in categories:
        if path.exists(root + '/' + category) == False:
            os.mkdir(root + '/' + category)

CreateFolders()

def SortToCategory(file):
    for format in imageFormats:
        if (file.endswith(format)):
            shutil.move(root + '/' + file, root + '/' + categories[0] + '/' + file)
            return True
    for format in appFormats:
        if (file.endswith(format)):
            shutil.move(root + '/' + file, root + '/' + categories[1] + '/' + file)
            return True
    for format in audioFormats:
        if (file.endswith(format)):
            shutil.move(root + '/' + file, root + '/' + categories[2] + '/' + file)
            return True
    for format in modelFormats:
        if (file.endswith(format)):
            shutil.move(root + '/' + file, root + '/' + categories[3] + '/' + file)
            return True
    for format in docFormats:
        if (file.endswith(format)):
            shutil.move(root + '/' + file, root + '/' + categories[4] + '/' + file)
            return True
    for format in videoFormats:
        if (file.endswith(format)):
            shutil.move(root + '/' + file, root + '/' + categories[5] + '/' + file)
            return True
    if file not in categories:
        if os.path.isdir(root + '/' + file):
            shutil.move(root + '/' + file, root + '/' + categories[6] + '/' + file)
            return True
        else:
            shutil.move(root + '/' + file, root + '/' + categories[7] + '/' + file)
    return False

for file in tqdm(os.listdir(root)):
    SortToCategory(file)