# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.daum.net/")
soup = BeautifulSoup(res.content, "html.parser")

# print(soup)

print("[ 다음 뉴스 - 메인 ]")
data = soup.select('#cSub div strong.tit_thumb')
for i, d in enumerate(data):    
    print(i+1, d.get_text().strip(), d.find('a')['href'])

print ("\n")

res = requests.get('https://finance.naver.com/sise/')
soup = BeautifulSoup(res.content, 'html.parser')

print ("[ 네이버 국내증시, 인기 검색종목 ]")
# a 태그이면서 href 속성 값이 특정한 값을 갖는 경우 탐색
data = soup.select("#popularItemList > li > a")
# print (data)

for item in data:
    print (item.get_text(), item['href'])

print ("\n")
print ("[ 네이버 주요 해외지수 ]")
data = soup.select("div.rgt > ul.lst_major > li")

for item in data:
    print ("지수이름:", item.find('a').get_text(), "현재지수:", item.find('span').get_text(), item.find('em').get_text())
