#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# YouTubeの字幕をxml方式でとってくる
#
# """

from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

#これを改造すればtimedtextの方も取ってこれる

def transcript(url):
    point = url[32:]
    lng = 'en'
    name = ''
    target = 'http://video.google.com/timedtext?hl=' + lng + '&lang=' + lng + '&name=' + name + '&v=' + point
    subtitles = urlopen(target)

    # html = urlopen(url)
    # soup = BeautifulSoup(html, 'html.parser')
    # urltitle = soup.find('title')
    # urltitle = urltitle.string

    translation = open('a.xml', 'wb')
    translation.write(subtitles.read())
    translation.close()


if __name__ == '__main__':
    print('Put the url')
    vidUrl = input('>>> ')
    transcript(vidUrl)
    print('finish!')
