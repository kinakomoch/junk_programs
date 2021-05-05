#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# 画像の向きを変える
#
# """

from PIL import Image
import glob
import os


def rotate(dir):
    files = glob.glob(os.path.join(dir, '*'))
    for file in files:
        img = Image.open(file)
        #180 rotation
        tmp = img.transpose(Image.ROTATE_90)
        tmp.save(file)

#This program must be played in the file which you wanna change
if __name__ == '__main__':
    import sys
    argv = sys.argv
    os.chdir(argv[1])
    rotate('./')
    print("finish")
