# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:49:59 2019

@author: DELL
"""
from baike_spider import url_manager, html_downloader, html_parser, html_outputer
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self,root_url):
        count = 1
        self.urls.add_url(root_url)
        while self.urls.has_new_url():
            try:
                print(count)
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 20:
                    break
                count = count + 1
            except:
                print("failed")
        self.outputer.output_mysql()
if __name__ =="__main__":
    root_url = "https://www.zhihu.com/people/koname/following"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

