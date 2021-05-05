'''
scanしたもので日付順にどうしてもソートできないもので名前を直す必要があるものを直す
'''
import os, glob, sys

def scanRename(dir):
    files = glob.glob(os.path.join(dir, '*'))

    for file in files:
        title = os.path.splitext(file)[0]
        ext = os.path.splitext(file)[1]
        os.rename(file, title + '-1' + ext)
        #-0 or -1で左右のページを表現する
        #そうするとページをスプリットするものが楽に扱える

if __name__ == '__main__':
    argv = sys.argv
    scanRename(argv[1])
