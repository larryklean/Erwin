import os


def print_sperator_line():
    print("====")


# 不同操作系统的斜线划分不同 根据操作系统不同会自动切换分隔符
print(os.path.join('usr', 'bin', 'spam'))

print_sperator_line()

# 显示当前目录
print(os.getcwd())
# 切换路径
# os.chdir('/Users/Cortana/')
print(os.getcwd())

print_sperator_line()

# 绝对路径和相对路径
# 绝对路径：从根目录开始
# 相对路径：相对于程序当前的工作目录
# . 当前路径
# .. 当前目录的父目录

# 创建目录
# os.mkdir('test')
# os.makedirs('a/b')

# 相对路径和绝对路径
print(os.path.abspath('.'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print_sperator_line()

# 切分目录区域
# 最后一个分隔符后为 basename
# 最后一个分隔符前为 dirname
path = os.path
print(path.dirname(os.path.abspath('.')))
print(path.basename(os.path.abspath('.')))

print_sperator_line()

# 获取当前系统的分隔符
print(os.path.sep)

print_sperator_line()

# 分割路径
print(os.path.abspath('.').split(os.path.sep))

print_sperator_line()

# 获取路径的大小
print(os.path.getsize(os.path.abspath('.')))

print_sperator_line()

# 列出当前目录下所有的文件 返回列表
print(os.listdir(os.path.abspath('.')))

print_sperator_line()

# 检验路径有效性
print(os.path.exists(os.path.abspath('.')))
print(os.path.isdir(os.path.abspath('.')))
print(os.path.isfile(os.path.abspath('.')))
