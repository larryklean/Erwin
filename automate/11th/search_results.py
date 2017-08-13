#! python3
# open several search results

import requests
import sys
import bs4
import webbrowser

print('Searching...')
res = requests.get('http://baidu.com/baidu?wd=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
bs_obj = bs4.BeautifulSoup(res.text, 'html.parser')
links = bs_obj.select('h3[class="t"] a')
# 少于5个则设置为5个
open_num = min(len(links), 5)
for index in range(open_num):
    # 调用默认浏览器 可以设置浏览器路径修改打开的浏览器
    webbrowser.open_new_tab(links[index].attrs['href'])
