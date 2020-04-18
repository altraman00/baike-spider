#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/18 15:18
# @Author: xk
# @File  : html_downloader.py
import urllib.request


class HtmlDownloader(object):

    # 下载html
    def download(self, url):
        if url is None:
            return

        response = urllib.request.urlopen(url)
        code = response.code

        if code != 200:
            return None

        return response.read().decode('utf-8')


# if __name__ == '__main__':
#     print("入口")
#     url = "https://baike.baidu.com/item/Python/407313"
#     dw = HtmlDownloader()
#     content = dw.download(url)
#     print('打印：', content, '\n')  # 打印

