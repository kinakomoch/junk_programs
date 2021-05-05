#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# ニュースを新しい順にcsvにまとめる
#
# """

from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

file = 'newslist.csv'

def getNews(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    #classなしのものだけ取るときは下のようなclass指定なしでやるといい
    cLists = []
    contents = soup.find('div', {'class': 'content'}).findAll('span', {'class': ''})[0:5]
    for content in contents:
        cLists.append(content.string)

    tLists = []
    for times in soup.findAll('div', {'class': 'date'})[0:5]:
        for time in times.findAll('time'):
            if time.has_attr('datetime'):
                tLists.append(time['datetime'])

    f = open(file, 'a')
    csvWriter = csv.writer(f)
    for i in range(0,5):
        row = [cLists[i], tLists[i]]
        print(row)
        csvWriter.writerow(row)

    f.close()
    #重複するデータがあった時に無視するとかしないといけない
    #重複しない最新のデータ（前の最新の時間より後のもの）をmail,snsで連絡

if __name__ == '__main__':
    url = 'https://www.example.com'
    getNews(url)
