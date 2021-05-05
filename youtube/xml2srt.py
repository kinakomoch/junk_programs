#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# xmlをsrtに方式に変換
#
# """

from bs4 import BeautifulSoup
import datetime, re


def xml2srt(xmlfile):
    f = open('a.srt', 'w')
    soup = BeautifulSoup(open(xmlfile + '.xml'), 'xml')
    count = 1
    for text in soup.findAll('text'):
        all = text.renderContents()
        start = text['start']
        dur = text['dur']
        string = text.string

        string = re.sub(r'&#39;', r"'", string)

        f.write(str(count) +'\n')
        count += 1

        dt = datetime.datetime(2000, 1, 1, 0, 0, 0, )    #年、月、日は使わないので適当
        start = dt + datetime.timedelta(seconds = float(start))    #開始時間を求める
        end = start + datetime.timedelta(seconds = float(dur))    #終了時間を求める
        st = start.strftime('%H:%M:%S,') + str(start.microsecond)[0:3]    #書式を合わせる
        et = end.strftime('%H:%M:%S,') + str(end.microsecond)[0:3]    #マイクロ秒の部分は最初の3ケタだけ
        f.write(st + ' --> ' + et + '\n')

        f.write(string + '\n')
        f.write('\n')

    f.close()


if __name__ == '__main__':
    xml2srt('a')
