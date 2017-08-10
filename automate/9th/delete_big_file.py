#! python3
# find size of file more than 50MB and delete them

import os


def find_big_paths(folder):
    paths = []
    for current_folder, sub_folders, filenames in os.walk(folder):
        print('Checking %s now...' % current_folder)
        for filename in filenames:
            if filename.startswith('.'):
                continue
            file_path = os.path.join(current_folder, filename)
            if os.path.getsize(file_path) > (50 * 1000 * 1000):
                paths.append(file_path)
    return paths


def delete_big_files(paths):
    if len(paths) == 0:
        print('no big file here')
        return
    for path in paths:
        os.unlink(path)
        print('%s has been deleted...' % os.path.basename(path))


path_list = find_big_paths('/Users/Cortana/PycharmProjects/Erwin/automate/9th/7月课堂录屏')
delete_big_files(path_list)
