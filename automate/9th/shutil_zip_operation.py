import shutil
import os
import zipfile

"""
print(os.path.dirname(os.getcwd()))
"""

# 两种方式打印出来的都是绝对路径
"""
print(os.getcwd())
print(os.path.abspath('.'))
"""

# 复制文件
# shutil.copy(source,destination)
# 1.将文件从source处复制到destination处 并返回复制后的地址
# 2.如果destination是一个文件名而非一个路径 则是复制后的名字
"""
shutil.copy('shutil.txt', 'shutil.txt')
"""

# 复制文件夹
# shutil.copytree(source,destination)
# 将整个文件夹从source地址复制到destination
"""
shutil.copytree('shutil_test', 'shutil_test_backup')
"""

# 移动
# shutil.move(source,destination)
# 1.将一个文件移动到另外一个位置
# 2.如果目标目录中存在同名文件的情况下会被覆盖
# 3.也可以同时移动并改名
# 4.可以改名
"""
shutil.move('shutil.txt', 'shutil_test')
"""

# 永久删除
# 1. os.unlink(path)删除path位置的文件
# 2. os.rmdir(path)删除path处的文件夹。此文件夹必须为空
# 3. os.rmtree(path)删除path处的文件夹，文件夹中的文件和文件夹都将被删除
"""
shutil.rmtree('shutil_test')
print(os.listdir('shutil_test'))
for file in os.listdir('shutil_test'):
    if file.endswith('.txt'):
        print(file)
        os.unlink(file)
"""

# 安全删除(第三方模块 send2trash)
# 不会直接永久删除文件而是删除到回收站
"""
send2trash.send2trash(path)
"""

# 遍历目录
# os.walk(folder)
# 遍历过程中每次返回三个东西
# 1.当前目录名称的字符串
# 2.当前目录中子目录的字符串列表
# 3.当前目录中文件的字符串列表
# 当前文件夹即为循环当前迭代的文件夹
"""
for foldername, subfolders, filenames in os.walk('/Users/Cortana/PycharmProjects/Erwin'):
    print('The current folder is %s' % foldername)
    for subfolder in subfolders:
        print(subfolder)
    print('-----')
    for filename in filenames:
        print(filename)
    print('===end===')
"""

# zip文件操作
# 首先要创建zip对象，类似于open打开的file对象
# 1.zipFile.ZipFile()创建zip文件对象
# 2.zipFile.nameList()获取zip中包含的所有文件名称列表
# 3.zipFile.getInfo(path)获取其中的某个文件
#   （1）file_size 原文件大小
#   （2）compress_size 压缩后的大小
"""
example_zip = zipfile.ZipFile('zips.zip')
print(example_zip.namelist())
file = example_zip.getinfo('Computer Networking.pdf')
print(file)
print(file.file_size)
print(file.compress_size)
print('ratio:%s' % str(file.file_size / file.compress_size))
example_zip.close()
"""

# 解压缩文件
# example_zip.extractAll(path)
# 1.不传入参数，将zip中的所有文件解压缩到当前目录
# 2.传入路径参数，将zip中的所有文件解压缩到指定目录
# exampleZip.extract(filename,path)
# 1.将zip中的指定文件进行解压缩到指定目录，不写第二个参数则解压到当前目录
# 2.返回被解压文件的绝对路径
"""
example_zip = zipfile.ZipFile('zips.zip')
example_zip.extractall()
example_zip.extract('Computer Networking.pdf')
example_zip.close()
"""

# 压缩文件
# 1.以写的方式创建压缩文件对象
# 2.调用写入方法进行文件的压缩
# 3.关闭资源
"""
old_zip = zipfile.ZipFile('zips.zip')
old_zip.extract('Computer Networking.pdf')
old_zip.close()

new_zip = zipfile.ZipFile('book_zip.zip', 'w')
new_zip.write('Computer Networking.pdf', compress_type=zipfile.ZIP_DEFLATED)
print(new_zip.namelist())
new_zip.close()
"""
