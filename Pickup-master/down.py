# -*- coding:utf-8 -*-
import re
import requests


def dowmloadPic(html):
    fp = open(string.encode('utf-8').decode('utf-8'), 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1

    resp = requests.get(start_urls)

    output = open('test.xls', 'wb')
    output.write(resp.content)
    output.close()


if __name__ == '__main__':
    # word = input("Input key word: ")
    url = 'http://api.worldbank.org/v2/zh/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel'
    result = requests.get(url)
    dowmloadPic(result.text)
