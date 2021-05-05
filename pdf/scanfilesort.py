#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# スキャン順に名前をちゃんとしたものにしてソート
#
# """

import os,os.path
import glob
import re

def scanfilesort():
    i=1
    files = glob.glob("*jpg")
    files.sort(key=os.path.getmtime, reverse=False)
    for file in files:
        if not re.search(r'im*\.jpg', file) and re.search('jpg', file):
            os.rename(file,'im{0:03d}.jpg'.format(i))
            i += 1

if __name__ == '__main__':
    import sys
    argv = sys.argv
    os.chdir(argv[1])
    scanfilesort()
