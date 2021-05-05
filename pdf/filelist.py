#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# ファイルの名前と取得時と更新時をcsvでまとめる
#
# """

import os, csv, time


def filelist():
    count = 0
    listFile = 'filelist.csv'
    dateFormat = '%Y/%m/%d %H:%M%S'

    # make a csv file
    csvFile = open(listFile, 'w', newline='')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["Name", "GetTime", "RenewTime"])


    files = os.listdir()
    files_dir = [f for f in files if os.path.isdir(f)]
    files_dir.sort()
    print(files_dir)

    for filename in files_dir:
        if os.path.isdir(filename) \
        and os.path.basename(__file__) != filename \
        and listFile != filename:

            gct = os.path.getctime(filename)
            gmt = os.path.getmtime(filename)

            row = []
            # file name
            row.append(filename)
            # the date of making files
            row.append(time.strftime(dateFormat, time.localtime(gct)))
            # the date of updating files
            row.append(time.strftime(dateFormat, time.localtime(gmt)))

            count += 1
            #write csv
            csvWriter.writerow(row)

    csvFile.close()
    print(count)

if __name__ == '__main__':
    filelist()
