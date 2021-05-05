#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# 取得時を新しい順に並べる
#
# """

import os, glob


def latestFile(dirname):
    os.chdir(dirname)
    files = glob.glob("*.jpeg")
    files.sort(key=os.path.getmtime, reverse=True)
    file = files[0]
    return file
#for i,name in enumerate(files):
#    if name.endswith("pdf"):
#        os.rename(name,str(i)+name)


if __name__ == '__main__':
    dirname = "./deepl"
    print(latestFile(dirname))
