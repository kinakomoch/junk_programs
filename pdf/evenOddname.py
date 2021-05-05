#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# スキャンの時に１枚の画像を２枚に分ける
# その際に名前が被らないようにする
# """


import glob, os

def even():
    even = 0
    files = glob.glob('*.jpg')
    files.sort(key=os.path.getmtime, reverse=False)
    for file in files:
        os.rename(file, 'im{0:03d}.jpg'.format(even))
        even += 2

def odd():
    odd = 1
    files = glob.glob('*.jpg')
    files.sort(key=os.path.getmtime, reverse=False)
    for file in files:
        os.rename(file, 'im{0:03d}.jpg'.format(odd))
        odd += 2

if __name__ == '__main__':
    import sys
    argv = sys.argv
    os.chdir(argv[1])
    odd()
