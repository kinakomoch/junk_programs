#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
#
#
# """


from PyPDF2 import PdfFileMerger, PdfFileReader
from PIL import Image
import glob, os, shutil, re, sys
from remove import rmJpg, rmPdf

def rename():
    Num = 1
    files = os.listdir()
    files.sort(key = os.path.getmtime, reverse = False)
    for file in files:
        #img*.jpgではなく、かつjpgであるものの名前をimg*.jpgへ変更
        if not re.search(r'img*\.jpg', file) and re.search('jpg', file):
            os.rename(file, 'img{0:03d}.jpg'.format(Num))
            Num += 1
        elif not re.search(r'img*\.jpeg', file) and re.search('jpeg', file):
            os.rename(file, 'img{0:03d}.jpg'.format(Num))
            Num += 1
        #png*.pngではなく、かつpngであるものの名前をpng*.pngへ変更
        elif not re.search(r'img*\.png', file) and re.search('png', file):
            os.rename(file, 'img{0:03d}.png'.format(Num))
            Num += 1
        elif not re.search(r'img*\.PNG', file) and re.search('PNG', file):
            os.rename(file, 'img{0:03d}.png'.format(Num))
            Num += 1
        else:
            pass


#とりあえず全ての画像を1枚ずつのpdfに
def img2pdf(path):
        lists = glob.glob(os.path.join(path, '*'))
        for list in lists:
            #拡張子だけ持ってくる
            ext = os.path.splitext(list)[1]
            if ext == '.pdf':
                continue
            elif ext == '.jpg' or '.jpeg' or '.png':
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
    name = pdfName + '.pdf'
    merger.write(name)
    os.mkdir('./pdfName')
    shutil.move(name, './pdfName')


def main():
    #注意点としてファイルの作成日順になってしまうので場合によってはimg2pdfとpdfmergeだけの
    #運用がいい場合がある
    argv = sys.argv
    os.chdir(argv[1])
    rename()
    img2pdf('./')
    pdfmerge('./', argv[2])
    rmJpg()
    rmPdf()

if __name__ == '__main__':
    main()
