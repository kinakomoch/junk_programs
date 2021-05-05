#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# 名前順に変更する
#
# """

import os
import glob
import shutil

def order(dirName, fileName):
    os.chdir(dirName)
    files = glob.glob('*' + fileName + '*')
    if not os.path.isdir(fileName):
        os.mkdir(fileName)
    for file in files:
        shutil.move(file, fileName)

#多分大丈夫だが危険性がある　精度を上げる際にisfileを使わないこと
#フォルダ名が入力したベースとなるファイル名になるのでできれば正確に入力して

if __name__ == '__main__':
    print('作業したいフォルダのパスを入れてくれ')
    fol_name = input('>>> ')
    print('ベースとなるファイル名を入れてくれ')
    pdf_name = input('>>> ')

    order(fol_name, pdf_name)
