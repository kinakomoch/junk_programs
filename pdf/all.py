#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# 更新順・時間順でpdfの作成を行う
# dファイルを作成しなければならない
#
#
# """


from img2pdf import img2pdf
from file_order import order
from remove import rmPdf, rmJpg
from rename import rename
from pdfmerge import pdfmerge
import os

if __name__ == '__main__':
    os.chdir('./d')
    rename()
    img2pdf('./')
    order('./','p')
    pdfmerge('./p','01')
    os.chdir('./p')
    rmJpg()
    rmPdf()
    os.chdir('../')
    os.rmdir('./p')
