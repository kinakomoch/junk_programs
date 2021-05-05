#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# pdf, jpg, mp4, xml, srt を削除
# フォルダ内のすべてのその形式のファイルを消す
# """

import glob,os

def rmPdf():
    files = glob.glob("*.pdf")

    for file in files:
        os.remove(file)

def rmJpg():
    files = glob.glob("*.jpg")

    for file in files:
        os.remove(file)

def rmMp4():
    files = glob.glob("*.mp4")

    for file in files:
        os.remove(file)

def rmXml():
    files = glob.glob("*.xml")

    for file in files:
        os.remove(file)

def rmSrt():
    files = glob.glob("*.srt")

    for file in files:
        os.remove(file)
