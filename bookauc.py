#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# オークションでの価格調査をcsvにまとめる
#
# """


import os, csv, time


def filelist():
    names = []
    with open("names.csv","r") as f:
        reader = csv.reader(f)
        for row in reader:
            names.append(row)

    csvFile = open('auction.csv', 'w', newline='')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["名前", "元値", "アマゾンの値段", "ヤフオク利益", "メルカリ利益", "ラクマ利益"])

    for namelist in names:
        for name in namelist:
            try:
                row = []
                # file name
                print(name)
                row.append(name)

                print("元値は")
                original = int(input("> "))
                row.append(original)

                print("amazonでは")
                amazon = int(input("> "))
                row.append(amazon)

                print("ヤフオクでは")
                yahoo = int(input("> ")) * 0.9 - 170
                row.append(yahoo)

                print("メルカリでは")
                mer = int(input("> ")) * 0.9 - 170
                row.append(mer)

                print("ラクマでは")
                rakuma = int(input("> ")) - 170
                row.append(rakuma)

                #write csv
                csvWriter.writerow(row)
            except:
                continue

    csvFile.close()

if __name__ == '__main__':
    filelist()
