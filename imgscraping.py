#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# サイトの画像をとってくる
# classとかの変更は毎度必要
# """

from urllib.request import urlretrieve, urlopen, Request
from bs4 import BeautifulSoup
import time
import sys
import os

def download(url):
    img = urlopen(url)
    localfile = open(os.path.basename(url), 'wb')
    localfile.write(img.read())
    img.close()
    localfile.close()


#あるフォルダでもないフォルダでもOK
def make_dir(dir_title):
    if not os.path.isdir(dir_title):
        os.mkdir(dir_title)
        os.chdir(dir_title)
    else:
        os.chdir(dir_title)


if __name__=='__main__':
    #URLをターミナルに記入 この方が便利かも？
    print('URLを入力してください')
    par_url = input('>>> ')
    res = urlopen(par_url)
    soup = BeautifulSoup(res, 'html.parser')
    
    print('保存フォルダ名を入れて')
    title = input('>>> ')
    make_dir(title)

    #２段階踏ませた方が精度が上がる　他の方法があれば変更
    for link in soup.findAll('div', {'class': 'more_body'}):
        for link2 in link.findAll('img', {'class': 'image pict'}):
            img_url = link2.get('src')
            print(img_url)
            download(img_url)
            time.sleep(2)

    print('終了しました')
