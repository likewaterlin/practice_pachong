# -*- coding: utf-8 -*-

# 这个网站我们需要爬走什么信息？

'''
<script>var props=(.*?)</script>
'''
import json
import re
import requests


class Kr36(object):
    def __init__(self):
        self.url = 'https://36kr.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        self.file = open('36kr.json', 'w')

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    # 分析的心得总结必须
    def parse_data(self, data):
        result = re.findall('<script>var props=(.*?)</script>', data, re.S)[0]

        temp = re.sub(',locationnal={.*', '', result)

        with open('temp.json', 'w') as f:
            f.write(temp)

        result_list = json.loads(temp)['feedPostsLatest|post']

        data_list = list()
        for result in result_list:
            temp = dict()
            temp['title'] = result['title']
            temp['cover'] = result['cover']
            data_list.append(temp)
        return data_list

    def save_data(self, data_list):
        for data in data_list:
            str_data = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(str_data)

    def __del__(self):
        self.file.close()

    def run(self):

        # 创建url
        # 创建请求头
        # 发送请求接受数据
        data = self.get_data(self.url)
        # 解析数据
        data_list = self.parse_data(data)
        # 保存数据
        self.save_data(data_list)


if __name__ == '__main__':
    kr36 = Kr36()
    kr36.run()
