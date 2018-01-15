# -*- coding: utf-8 -*-

# 创建url
# 创建headers
# 设置参数
# 响应数据
# 保存源码

# 面向对象
import requests
import sys


class Baidu():

    def __init__(self,name,pn):
        self.name = name
        self.base_url = 'https://tieba.baidu.com/f?kw={}&pn='.format(name)
        self.url_list = [self.base_url + str(i*50) for i in range(pn)]
        # for i in range(pn):
        #     url = self.base_url + str(i*50)
        #     self.url_list.append(url)
        # print(self.url_list)

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'
        }

    def get_data(self,url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def save_data(self,data, num):
        filename = self.name + '_' + str(num) + '.html'

        with open(filename,'wb') as f:
            f.write(data)

    def run(self):

        for url in self.url_list:
            data = self.get_data(url)
            num = self.url_list.index(url)
            self.save_data(data, num)

if __name__ == '__main__':
    name = sys.argv[1]
    pn = int(sys.argv[2])
    baidu = Baidu(name, pn)
    baidu.run()