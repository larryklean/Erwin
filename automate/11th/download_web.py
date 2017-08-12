#! python3
# download text from web by requests

import webbrowser
import requests

# webbrowser打开浏览器
"""
webbrowser.open('http://www.baidu.com/')
"""

# requests下载文件
"""
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
"""

# type()函数返回获取数据的类型
"""
print(type(res))
"""

# status_code 200、404、500...
"""
print(res.status_code == requests.codes.ok)
"""

# 错误检查
# 也可以调用response的raise_for_status()进行抛出,失败时会自动停止
# 如果问题不是十分严重则可以用try...except Exception as...进行异常抛出
"""
res.raise_for_status()
"""

# text获取response返回的文本数据
"""
print(len(res.text))
print(res.text[:250])
"""

# 将下载后的文本保存到本地，需要使用write()方法
# 但是需要将文本转换为unicode编码再进行存储（'wb'参数）,即便下载的内容是纯文本
# xxx.iter_content(size)遍历出字节的数量
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
# if res.status_code == requests.codes.ok:
with open('download_text.txt', 'wb') as download_file:
    for chunk in res.iter_content(100000):
        download_file.write(chunk)

