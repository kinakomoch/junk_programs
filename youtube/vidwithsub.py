#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# mp4に字幕を入れる
# """

from ydl import download
from xml2srt import xml2srt
from ytranscript import transcript
from bs4 import BeautifulSoup
from rename import youname
import os, glob, shutil


def main(num):
    print("url入れて")
    input_url = input(">>> ")
    target = input_url
    download(target)
    os.chdir('./youtube')
    youname()
    transcript(target)
    xml2srt('a')
    # os.systemはターミナルでのコマンド実行を行うことが可能
    os.system('ffmpeg -i a.mp4 -vf subtitles=a.srt cs{0:03d}.mp4'.format(num))
    shutil.move('cs{0:03d}.mp4'.format(num), '../')
    os.remove('./a.mp4')
    os.remove('./a.srt')
    os.remove('./a.xml')

if __name__ == '__main__':
    print("何番?")
    number = int(input(">>> "))
    main(number)
