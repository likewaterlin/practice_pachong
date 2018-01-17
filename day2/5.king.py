# -*- coding: utf-8 -*-

import requests
import sys
import json


class King_trans(object):
    def __init__(self, word):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.headers = {

            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'

        }
        self.post_data = {
            'f': 'auto',
            't': 'auto',
            'w': word
        }

    def get_data(self):
        response = requests.post(self.url, data=self.post_data, headers=self.headers)
        return response.content.decode()

    # 本句的构成理解不够深刻
    def parse_data(self, data):
        dict_data = json.loads(data)
        print(dict_data['content']['out'])

    def run(self):
        # 构建发送请求的url
        # 构建请求头
        # 构建post数据
        # 发送请求，获取响应
        data = self.get_data()
        # 解析响应
        self.parse_data(data)


if __name__ == '__main__':
    king = King_trans(sys.argv[1])
    king.run()
