#!/usr/local/bin/python
# coding: gbk
from bs4 import BeautifulSoup
import requests
import re
import xlwt


url = r'https://pf.53shop.com/m/pifashichang/sc10-1.html'

source = requests.get(url)
source.encoding = 'gbk'
source = source.text
soup = BeautifulSoup(source, 'lxml')

''''for hott in soup.find_all('h3', class_= 'hott'):
    name = hott.a.text
    print(name)'''''

info = r'<h3 .*?>(.*?)</h3>'
m_tr =  re.findall(info,source,re.S|re.M)

print(type(source))
namlist = []

for line in m_tr:
    name = r'<a href=.*?>(.*?)</a>'
    link = r'<a href="(.*?)">.*?</a>'
    nam = re.findall(name,line,re.S|re.M)
    link = re.findall(link,line,re.S|re.M)
    u = link[0]
    abs = requests.get(u)
    abs.encoding = 'gbk'
    abs = abs.text
    content = r'<div class="content">(.*?)</div>'
    con = re.findall(content,abs,re.S|re.M)
    #print(nam)
    #print(namlist)
    print(u)
    #print(con)
    if re.search('油', con[0]) != None:
        print(nam)
        namlist.extend(nam)
    else:
        print('0')

print(namlist)


def excel_save(file_path, namlist):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    i = 0
    for n in namlist:
        for j in range(len(namlist)):
            sheet1.write(i,j,namlist[j])
        i = i + 1

    f.save(file_path)

excel_save('name.xls',namlist)