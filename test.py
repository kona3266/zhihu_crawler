## -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from baike_spider import url_manager, html_downloader, html_parser, html_outputer
#response = urlopen("https://www.zhihu.com/people/koname/following")
#html = response.read()
#soup = BeautifulSoup(html,'html.parser',from_encoding = 'utf-8')
#res_data = {}
#name_node = soup.find('h1',class_="ProfileHeader-title").find('span',class_ ="ProfileHeader-name" )
#res_data['name'] = name_node.get_text()
#follower_num = soup.find('a', class_ = "NumberBoard-item",href = re.compile(r'followers$')).find('strong',class_='NumberBoard-itemValue')
#res_data['follower'] = follower_num.get_text()
#edu_info = soup.find_all('div',class_="ProfileHeader-infoItem")
#res_data['edu'] = edu_info[1].get_text()
#new_urls = set()
#links = soup.find_all('a',href = re.compile(r'www.zhihu.com/people/'))
#for link in links:
#    new_url = link['href']
#    new_full_url = "https:"+new_url+"/following"
#    new_urls.add(new_full_url)
#res_data = {'name':'koname','follower':15,'edu':'hust'}
#import mysql.connector
#conn = mysql.connector.connect(user='root',password='a66b01c06',database='spider')
#cursor = conn.cursor()
#sql = ('insert into zhihu' 
#       '(name, follower,edu)' 
#       'values (%s, %s, %s)')
#data = (res_data['name'],res_data['follower'],res_data['edu'])
#cursor.execute(sql,data)
#conn.commit()
downloader = html_downloader.HtmlDownloader()
parser = html_parser.HtmlParser()
new_url = 'https://www.zhihu.com/people/koname/following'
html_cont = downloader.download(new_url)
new_urls,new_data = parser.parse(new_url,html_cont)
print(new_data)
#import mysql.connector
#conn = mysql.connector.connect(user='root',password='a66b01c06',database='spider')
#cursor = conn.cursor()
#sql = ('insert into zhihu' 
#      '(name, follower,edu)' 
#      'values (%s, %s, %s)')
#sql_in = (new_data['name'],new_data['follower'],new_data['edu'][0]['school']['name'])
#
#cursor.execute(sql,sql_in)
#conn.commit()