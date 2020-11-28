# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:49:59 2019

@author: DELL
"""
from baike_spider import url_manager, html_downloader, html_parser, html_outputer
from file_formater import format_result
class SpiderMain(object):
    def __init__(self, root_url):
        self.urls = url_manager.UrlManager()
        self.root_url = root_url
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self):
        count = 1
        self.urls.add_url(self.root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
                count = count + 1
            except Exception as e:
                print("craw url failed: %s" % e)
if __name__ =="__main__":
    print('Enter you username:')
    username = input()
    root_url = "https://www.zhihu.com/people/%s/following/" % username
    spider = SpiderMain(root_url)
    spider.craw()
    format_result()


