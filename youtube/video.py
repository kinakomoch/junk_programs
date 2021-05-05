#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# youtube以外のサイトの動画をとってくる
# 使用毎に多少の変更が必要
# """

from urllib.request import urlretrieve, urlopen, Request
from bs4 import BeautifulSoup
import time
import sys
import os.path
import os

def download(url):
    video = urlopen(url)
    localfile = open(os.path.basename(url), 'wb')
    localfile.write(video.read())
    video.close()
    localfile.close()

par_url = ''

res = urlopen(par_url)
soup = BeautifulSoup(res, 'html.parser')

os.mkdir('猫')
os.chdir('./猫')
for link in soup.find_all('source', {'type': 'video/mp4'}):
    video_url = link.get('src')
    print(video_url)
    download(video_url)
    time.sleep(2)
