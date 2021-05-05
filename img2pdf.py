#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# jpegをpdfに変更
#
# """

from PIL import Image
import os
import shutil
import re
import glob


#とりあえず全ての画像を1枚ずつのpdfにする
def img2pdf(dir):
        lists = glob.glob(os.path.join(dir, '*'))
        for list in lists:

            #拡張子だけ持ってくる
            ext = os.path.splitext(list)[1]


            if ext == '.pdf':
                continue
            elif ext == '.jpg' or '.png':
                im = Image.open(list)
                if im.mode == 'RGBA':
                    im = im.convert('RGB')
                pdf_file = str(list).replace(ext, '.pdf')
                im.save(pdf_file, 'PDF', resolution = 100)
            else:
                continue



if __name__ == '__main__':
    print('フォルダ名を入れろ')
    dir1 = input('>>> ')
    img2pdf(dir1)
