# -*- coding: utf-8 -*-
import requests
class HtmlDownloader(object):
    def download(self, url):
        headers = {'Referer':'https://www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
        if url is None:
            return None
        response = requests.get(url,headers = headers)
        if response.status_code !=200:
            return None
        return response.text