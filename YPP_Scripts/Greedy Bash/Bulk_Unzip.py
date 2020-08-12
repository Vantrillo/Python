import glob, os
from zipfile import ZipFile

path = '/home/malcyan/Downloads/allporncomic.com'
os.chdir(path)
for file in glob.glob('*.zip'):
    name = file.split('.')[0]
    with ZipFile(file,'r') as zip:
        zip.extractall(name)