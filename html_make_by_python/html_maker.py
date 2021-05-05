#!/usr/bin/python
# -*- coding: utf-8 -*-

def html_maker(lang, title, content):
    html_source = '''
    <!DOCTYPE html>
    <html lang='{0}'>
    <head>
    <meta charset='UTF-8'>
    <title>{1}</title>
    </head>
    <body>{2}</body>
    </html>
    '''.format(lang, title, content)

    return html_source


if __name__ == '__main__':

    lang = 'ja'
    title = '今日の晩御飯'
    content = '''本日の晩御飯は味噌汁一杯、<h1>食パン４枚</h1>
    <br>りんご50個
    <img src = "./apple.jpg", width="60", height="60>"'''
    html = html_maker(lang, title, content)


    with open('index.html', 'w') as html_file:
        html_file.write(html)
