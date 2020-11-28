# -*- coding: utf-8 -*-

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def collect_data(self,data):
        if data is None:
            return
        self.write_to_file(data)
    def write_to_file(self, data):
        with open('result.txt', 'a+') as f:
            f.write("{0}\n".format(data))
            f.close()