#   Jeff W. Ferrell 10/9/17
#   Python Course, item 63 of 68
#   Copy .txt files from one folder to another
#   Made with Python 2.7 with datetime module

import shutil
import os


source = '\Users\Student\Desktop\Folder_A'
folder = os.listdir(source)
destination = '\Users\Student\Desktop\Folder_B'

for files in folder:
    if files.endswith('.txt'):
        shutil.move(os.path.join(source, files),os.path.join(destination))






