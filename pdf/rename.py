#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# 名前の変更
#
# """

import os,re,sys,glob

def rename():
    Num = 1
    files = os.listdir()
    for file in files:
        #img*.jpgではなく、かつjpgであるものの名前をimg*.jpgへ変更
        if not re.search(r'img*\.jpg', file) and re.search('jpg', file):
            os.rename(file, 'img{0:03d}.jpg'.format(Num))
            Num += 1
        elif not re.search(r'img*\.jpeg', file) and re.search('jpeg', file):
            os.rename(file, 'img{0:03d}.jpg'.format(Num))
            Num += 1
        #png*.pngではなく、かつpngであるものの名前をpng*.pngへ変更
        elif not re.search(r'img*\.png', file) and re.search('png', file):
            os.rename(file, 'img{0:03d}.png'.format(Num))
            Num += 1
        else:
            pass

def youname():
    files = glob.glob('*.mp4')
    for file in files:
        if not re.search(r'cs*\.mp4', file):
            os.rename(file, 'a.mp4')

if __name__ == '__main__':
    print("この場所からの目的のフォルダのパスを入れてください")
    os.chdir(input('>>> '))
    rename()
    print("終わり")
