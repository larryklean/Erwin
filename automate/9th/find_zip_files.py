import os
import zipfile


def find_py_files(folder):
    path_list = []
    full_path = os.path.abspath(folder)
    print(full_path)
    for current_folder, subfolders, filenames in os.walk(full_path):
        if os.path.basename(current_folder).startswith('.'):
            continue
        for filename in filenames:
            if not filename.endswith('.py'):
                continue
            compress_path = os.path.join(current_folder, filename)
            path_list.append(compress_path)
    return path_list


def compress_into_zip(path_list):
    py_zip = zipfile.ZipFile('pys.zip', 'w')
    for path in path_list:
        py_zip.write(path, compress_type=zipfile.ZIP_DEFLATED)
    py_zip.close()


paths = find_py_files('/Users/Cortana/PycharmProjects/Erwin')
compress_into_zip(paths)
