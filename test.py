## -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from baike_spider.html_downloader import HtmlDownloader
from baike_spider.html_parser import HtmlParser
downloader = HtmlDownloader()
parser = HtmlParser()
new_url = 'https://www.zhihu.com/people/koname/following'
html_cont = downloader.download(new_url)
new_urls,new_data = parser.parse(new_url,html_cont)
print(new_data)