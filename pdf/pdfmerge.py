#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pdfをまとめる

from PyPDF2 import PdfFileMerger, PdfFileReader
import glob
import os


def pdfmerge(path, pdfName):

    pdfFile = glob.glob(path + '/*.pdf')
    pdfFile.sort()

    merger = PdfFileMerger()
    for filename in pdfFile:
        merger.append(PdfFileReader(filename, 'rb'))

    merger.write(pdfName + '.pdf')


if __name__ == '__main__':
    print("フォルダまでのパスを入れてくれ")
    print("ただし最後の/は要らない")
    dir_path = input(">>> ")
    print("pdfの名前何にする？")
    print(".pdfは要らない")
    pName = input(">>> ")
    pdfmerge(dir_path, pName)
    print("終わり")
