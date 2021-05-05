#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# mp4をmp3に変える
#
# """

from ydl import download
from ffmpeg import convert
from remove import rmMp4
import os, glob

if __name__ == '__main__':
    print("Input url")
    url = input(">>> ")
    download(url)
    os.chdir("./youtube/")
    fnames = glob.glob("*.mp4")
    for fname in fnames:
        bname =  os.path.splitext(fname)[0]
        convert(fname, bname + '.mp3')
        rmMp4()
        print("Next")
    print("finish")
