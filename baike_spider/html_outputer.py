# -*- coding: utf-8 -*-
import mysql.connector
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    def output_mysql(self):
        conn = mysql.connector.connect(user='root',password='a66b01c06',database='spider')
        cursor = conn.cursor()
        sql = ('insert into zhihu' 
       '(name, follower,edu)' 
       'values (%s, %s, %s)')
        for data in self.datas:
            try:
                sql_in = (data['name'],data['follower'],data['edu'][0]['school']['name'])
            except:
                sql_in = (data['name'],data['follower'],'')
            cursor.execute(sql,sql_in)
        conn.commit()