import shelve

# 1.open打开文件
# 2.进行读或写操作 read write
# 3.关闭文件 close

# 向文件中写入数据
# w模式 会覆盖掉文件中的原有内容
# a模式 会在基础之上进行追加
hello_file = open('madlibs.txt', 'w')
# hello_file = open('madlibs.txt', 'a')
hello_file.write('hello')
hello_file.close()

# 从文件中读取数据
# read() 将整个文件中的数据作为一个字符串取出
# readLines() 将文件中的数据作为多行读取，每一行结尾增加了换行
hello_file2 = open('madlibs.txt')
text = hello_file2.read()
print(text)
hello_file2.close()

# 操作文件和关闭一起执行
with open('madlibs.txt') as file:
    print(file.read())

# 使用shelve保存数据
# shelve使用方式与字典相近，OSX会在当前文件夹下生成一个.db文件
shelf_field = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelf_field['cats'] = cats
shelf_field.close()

shelf_field = shelve.open('mydata')
print(type(shelf_field))
print(shelf_field['cats'])
shelf_field.close()

with shelve.open('mydata') as shelf_field:
    print(shelf_field['cats'])
