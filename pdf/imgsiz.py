#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# 画像の大きさを表示
#
# """

from PIL import Image

def imgsize(img):
    im = Image.open(img)
    size = im.size
    width = size[0]
    height = size[1]
    print(width, height)


if __name__ == '__main__':
    print('Input the image path')
    pict = input('>>> ')
    imgsize(pict)
