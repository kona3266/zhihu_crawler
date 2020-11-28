# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
import json
class HtmlParser(object):
    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a',href = re.compile(r'//www.zhihu.com/people/'))
        for link in links:
            new_url = link['href']
            new_full_url = "https:"+new_url+"/following"
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self,page_url,html_cont):
        res_data = {}
        id = "".join(re.findall(r"people/(.+?)/following",page_url))
        expr = re.compile(r'<script id="js-initialData".*?</script>',re.M)
        data = expr.search(html_cont).group()
        raw_info = json.loads(re.search(r'{.*}',data).group())
        info = raw_info['initialState']['entities']['users']
        res_data['name'] = info[id]['name']       
        res_data['follower'] = info[id]['followerCount']       
        res_data['edu'] = info[id]['educations']
        return res_data
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding = 'utf-8')
        new_urls  = self._get_new_urls(page_url,soup)
        new_data  = self._get_new_data(page_url,html_cont)
        
        return new_urls,new_data
        