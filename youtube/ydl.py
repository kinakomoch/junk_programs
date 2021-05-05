#!/usr/bin/env python
# -*- coding: utf-8 -*-
# """
# YouTubeのダウンロード(mp4)
#
# """

from pytube import YouTube
import os


def download(url):
    yt = YouTube()
    yt.url = url

    for video in yt.get_videos():
        print(video)

    if not os.path.exists('youtube'):
        os.mkdir('youtube')
    try:
        video = yt.get('mp4', '360p')
        video.download('./youtube/')
    except:
        print("error")

if __name__ == '__main__':
    print("url入れて")
    input_url = input(">>> ")
    target = input_url
    download(target)
