#! python3
# copies an entire folder and its contents into a ZIP file whose filename increment

import zipfile
import os


def back2zip(folder):
    fullpath = os.path.abspath(folder)
    number = 1
    # what files already exsits
    while True:
        zip_filename = os.path.basename(fullpath) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1
    # create new zip file
    print('Creating %s...' % zip_filename)
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    for foldername, sudfolders, filenames in os.walk(folder):
        print('Add files in %s...' % foldername)
        # add current folder to zip file
        backup_zip.write(foldername)
    for filename in filenames:
        pass
        # TODO: