# -*- coding: utf-8 -*-

# 这个网站我们需要爬走什么信息？title?url?image?text?或者其他的什么信息
import json

from lxml import etree

import requests


class Baidu(object):
    def __init__(self):
        # 初始值除了url headers还需要哪些数据？headers的过新或者过旧是否导致数据下载或者获取有问题？
        self.url = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.url_list = None

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        }
        # 有开就有关
        self.file = open('qiushi.json', 'w')

    # 获取一共就13页的url
    def generate_url_list(self):
        self.url_list = [self.url.format(i) for i in range(1, 14)]

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        # print(response.content,type(response.content)) 得出的是bytes类型的数据
        # print(response.content.decode(),type(response.content.decode()))得出的是str类型的数据
        return response.content

    def parse_data(self, data):
        # 获得的数据包含那些？需要提取那些信息？
        # 需要对获取的数据做哪些操作？能否提出一些例子？
        '''
        一般根据需求来的。获取的数据是否需要进行转换？
        1--是否需要将html源码转换成element对象？
        如果需要的话通过html = etree.HTML(data)实现
        2--是否需要通过json来转换？--判断标准是什么？
        '''
        html = etree.HTML(data)
        # 定位出帖子节点列表
        node_list = html.xpath('//*[contains(@id,"qiushi_tag_")]')
        # 构建存放返回数据的列表
        data_list = []
        # 遍历节点列表，从没一个节点中抽取数据
        for node in node_list:
            temp = dict()
            # 重点分析
            try:
                temp['user'] = node.xpath('./div[1]/a[2]/h2/text()')[0].strip()
                temp['link'] = 'https://www.qiushibaike.com' + node.xpath('./div[1]/a[2]/@href')[0]
                temp['age'] = node.xpath('./div[1]/div/text()')[0]
                temp['gender'] = node.xpath('./div[1]/div/@class')[0].split(' ')[-1].replace('Icon', '')
            except:
                temp['user'] = '匿名用户'
                temp['link'] = None
                temp['age'] = None
                temp['gender'] = None
            data_list.append(temp)

        return data_list

    def save_data(self, data_list):
        # 如何进行数据的保存？
        # with open('xxx','wb')as f:
        #       f.write(xxx)
        # 保存数据有什么问题存在？

        for data in data_list:
            str_data = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(str_data)

    def __del__(self):
        self.file.close()

    def run(self):
        # 创建url
        # 创建请求头

        # 遍历url列表
        self.generate_url_list()

        for url in self.url_list:
            # 发起请求获取响应
            data = self.get_data(url)

            # 解析数据  解析有很多种，需要分析爬下来的信息的类型
            data_list = self.parse_data(data)
            # 保存数据
            self.save_data(data_list)

            # 下载数据,需要什么条件才能进行下载呢，是链接 呢 ？


            # 在最后看看是否需要重复爬取数据呢？


if __name__ == '__main__':
    baidu = Baidu()
    baidu.run()

    # 难点：得对这老师的代码抄，因为不知道怎么继续下去，没有自己的思路
    # 确切点说不知道自己拿的是什么数据，又可以拿这些数据干什么。
    '''
    好那么我们来分析一下这个问题：
    不知道拿什么数据：
    通过generate_url_list 我们拿到了所有的链接
    通过get_data 我们拿到了所有链接对应的源代码
    通过parse_data解析数据 我们拿到源代码了含有的我们需要的链接
    通过save_data 我们拿到了数据
    这是一个过滤的过程，在过滤的过程中我们能够用到什么工具？xpath？selenium？queue?etc.

    '''
