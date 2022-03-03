#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   collectArticles.py
@Time    :   2022/03/03 13:39:17
@Author  :   y0lo 
@Desc    :   自动爬取hexo博客文章和csdn博客文章
'''

# here put the import lib
import requests
import re
import json

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}

def add_info(f):
    info_str = """**一个19级的小菜鸡**<br>
[![我的 GitHub 数据](https://github-readme-stats.vercel.app/api?username=y0lo-0924)]()<br>
""" 
    f.write(info_str)

def add_hexo(f):
    f.write('\n## 我的hexo文章\n')
    hexo_url="https://y0lo-0924.github.io/content.json"
    r = requests.get(hexo_url,headers)
    json_hexo = json.loads(r.text)
    for json_str in json_hexo:
        str1 = '- [{0}]({1})\n'
        f.write(str1.format(json_str['title'],'http://y0lo-0924.github.io/'+json_str['path']))
        print(json_str['title'])

def add_csdn(f):
    f.write('\n## 我的CSDN文章\n')

if __name__ == '__main__':
    f = open('README.md','w')
    add_info(f)
    f.write('<table><tr>\n')
    f.write('<td>\n')
    add_hexo(f)
    f.write('\n</td>\n')
    f.write('<td>\n')
    add_csdn(f)
    f.write('\n</td>\n')
    f.write('</tr></table>\n')
    f.flush()
    f.close()