## a program to oragnise the file directory

import os
from pathlib import Path

Subdir = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIOS": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pick_dir(value):
    for dir_, type_ in Subdir.items():
        if value in type_:
            return dir_
    return "MISC"

def arrange_dir():
    for item in os.scandir():
        if item.is_dir():
            continue
        f = Path(item)
        f_Type = f.suffix.lower()
        directory = pick_dir(f_Type)
        dir_Path = Path(directory)
        if dir_Path.is_dir() != True:
            dir_Path.mkdir()
        f.rename(dir_Path.joinpath(f))
arrange_dir()