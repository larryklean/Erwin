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
        # add files in current folder to zip file
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            print('Add %s ...' % filename)
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print('Done')


back2zip('/Users/Cortana/PycharmProjects/Erwin/automate/8th')
