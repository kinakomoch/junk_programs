#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# 名前順に１つのpdfにまとめる
#
# """


from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader
import os, shutil, re, glob, sys


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

def pdfmerge(path, pdfName):
    pdfFile = glob.glob(path + '/*.pdf')
    pdfFile.sort()

    merger = PdfFileMerger()
    for filename in pdfFile:
        merger.append(PdfFileReader(filename, 'rb'))

    merger.write(pdfName + '.pdf')

if __name__ == '__main__':
    argv = sys.argv
    os.chdir(argv[1])
    img2pdf("./")
    name = argv[2]
    pdfmerge("./", name)
    shutil.move(name + '.pdf', "../")
