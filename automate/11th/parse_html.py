#! python3
# parse html file by beautifulsoup4

import requests
import bs4

# 下载了网页之后可以使用beautifulsoup进行html解析
# 需通过pip进行安装，导入名为bs4模块 即beautifulsoup第四版
# bs4需要先创建一个对象，参数为要解析的HTML(网址或者相应的文件对象),同时也需要指定解析器parser,否则会有警告
example = open('example.html')
bs_obj = bs4.BeautifulSoup(example, 'html.parser')
# print(type(bs_obj))
# 使用select方法进行标签的查找，参数是一个字符串的查找规则（类似于正则表达式），返回一个列表
# 可以使用str()转换为字符串
# 可以调用attrs返回tag对应的属性字典
"""
elems = bs_obj.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(type(str(elems[0])))
print(elems[0].attrs)
elems = bs_obj.select('p')
print(elems[0])
print(elems[0].getText())
"""
# 使用属性获取元素
span_elem = bs_obj.select('span')[0]
print(span_elem)
print(span_elem.get('id'))
print(span_elem.attrs)
