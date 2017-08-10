#! python3
# compress all files of specify folder into a zip file

import os
import zipfile


def backup2zip(folder_path):
    full_path = os.path.abspath(folder_path)
    base_name = os.path.basename(full_path)
    number = 1
    while True:
        zip_file_name = base_name + '_' + str(number) + '.zip'
        if not os.path.exists(zip_file_name):
            break
        number = number + 1
    current_zip = zipfile.ZipFile(zip_file_name, 'w')
    for current_folder, sub_folders, filenames in os.walk(full_path):
        print('Adding files of %s into zip...' % current_folder)
        current_zip.write(current_folder, compress_type=zipfile.ZIP_DEFLATED)
        for filename in filenames:
            new_base = base_name + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            print('Adding file %s into zip' % filename)
            current_zip.write(os.path.join(current_folder, filename), compress_type=zipfile.ZIP_DEFLATED)
    current_zip.close()
    print('Compress done')


backup2zip('/Users/Cortana/PycharmProjects/Erwin/automate/8th')
