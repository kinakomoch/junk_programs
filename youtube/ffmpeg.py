#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# (例として)mp4をmp3にする
# """

import ffmpy, os

def convert(ip, op):
    ff = ffmpy.FFmpeg(
        inputs={ip : None},
        outputs={op : None}
    )
    #ff.cmd
    ff.run()

if __name__ == '__main__':
    os.chdir("./youtube")
    print("変換前のファイル名を入力")
    i = input(">>> ")
    print("変換後のファイル名を入力")
    o = input(">>> ")
    convert(i, o)
