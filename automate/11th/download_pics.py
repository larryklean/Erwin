#! python3
# download comics in website

import requests
import bs4
import os

base_url = 'https://xkcb.com'
url = 'https://xkcd.com'
if not os.path.exists('comics'):
    os.mkdir('comics')
while not url.endswith('#'):
    print('current url %s' % url)
    # 下载页面
    res = requests.get(url)
    res.raise_for_status()
    # 解析页面的图片
    bs_obj = bs4.BeautifulSoup(res.text, 'html.parser')
    comic_pic = bs_obj.select('div[id="comic"] img')[0]
    if comic_pic is None:
        print('No img show')
        break
    # 拼接图片的链接地址 用于图片下载
    comic_link = 'https:' + comic_pic.get('src')
    print('Downloading page %s' % comic_link)
    # 下载图片
    res_pic = requests.get(comic_link)
    res_pic.raise_for_status()
    save_path = os.path.join('comics', os.path.basename(comic_link))
    # 保存下载图片到本地
    with open(save_path, 'wb') as pic_file:
        for chunk in res_pic.iter_content(1024 * 10):
            pic_file.write(chunk)
    # 更新url
    href_append = bs_obj.select('a[rel="prev"]')[0].get('href')
    url = base_url + href_append

print('Done')
