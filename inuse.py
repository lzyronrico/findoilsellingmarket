#!/usr/local/bin/python
# coding: gbk
from bs4 import BeautifulSoup
import requests
import re
import xlwt

namlist = []
for page in range(1,54):
    url = url = r'https://pf.53shop.com/m/pifashichang/sc10-'+str(page)+'.html'
    source = requests.get(url)
    source.encoding = 'gbk'
    source = source.text
    soup = BeautifulSoup(source, 'lxml')
    info = r'<h3 .*?>(.*?)</h3>'
    m_tr = re.findall(info, source, re.S | re.M)
    for line in m_tr:
        name = r'<a href=.*?>(.*?)</a>'
        link = r'<a href="(.*?)">.*?</a>'
        nam = re.findall(name, line, re.S | re.M)
        link = re.findall(link, line, re.S | re.M)
        u = link[0]
        abs = requests.get(u)
        abs.encoding = 'gbk'
        abs = abs.text
        content = r'<div class="content">(.*?)</div>'
        con = re.findall(content, abs, re.S | re.M)
        if re.search('油', con[0]) != None:
            print(nam)
            namlist.extend(nam)
        else:
            print('0')

print(namlist)