# -*- coding: utf-8 -*-

# 这个网站我们需要爬走什么信息？ 获取了title信息和url信息，以及url下的image图片信息
import os

import requests

from lxml import etree


class Baidu(object):
    def __init__(self, name):
        self.url = 'https://tieba.baidu.com/f?ie=utf-8&kw={}'.format(name)
        # 由于浏览器版本太高导致的支持ajax，我们要的信息都被注释掉了，可以通过低版本的浏览器进行获取数据，也可以考虑用正则
        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'
        }

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        # print(response.content,type(response.content)) 得出的是bytes类型的数据
        # print(response.content.decode(),type(response.content.decode()))得出的是str类型的数据
        # 获得的数据包含那些？需要提取那些信息？
        # print(response.content.decode())
        return response.content

    def parse_list_page(self, data):
        # 将html源码转换成element对象
        html = etree.HTML(data)
        # 获取所有li下面的该节点
        # 里面的@class=""是为了筛选掉广告的列表
        node_list = html.xpath('//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')
        # print(node_list)单页我获取了47个我需要的信息通过debug的信息
        # 将其保存在一个列表上 需要通过遍历的形式通过

        data_list = list()

        for node in node_list:
            temp = dict()
            # 下面的这个xpath是如何形成的？
            # 获取href信息，得到的信息是一个列表，所以在后面用[0]取出
            temp['url'] = 'http://tieba.baidu.com' + node.xpath('./@href')[0]
            # 获取文本信息
            temp['title'] = node.xpath('./text()')[0]
            # print(temp)
            data_list.append(temp)
        print(data_list)
        next_node = html.xpath('//*[@id="frs_list_pager"]/a[last()-1]/@href')
        next_url = 'http:' + next_node[0] if len(next_node) > 0 else None

        # 返回值
        return data_list, next_url

    def parse_detail_page(self, data):
        html = etree.HTML(data)

        image_list = html.xpath("//cc/div[contains(@id,'post_content_')]/img/@src")

        return image_list

    def download(self, image_list):
        if not os.path.exists('image'):
            os.makedirs('image')
        for url in image_list:
            file_name = 'image' + os.sep + url.split('/')[-1]
            data = self.get_data(url)
            with open(file_name, 'wb')as f:
                f.write(data)

    def run(self):

        # 创建url
        # 创建请求头
        # 发送请求接受数据
        next_url = self.url

        while next_url:
            # 发送请求获取响应(获取列表页面的响应)
            data = self.get_data(next_url)

            # 从响应中抽取详情页面的数据列表，下一页链接
            data_list, next_url = self.parse_list_page(data)

            # 编列列表，发起请求(获取详情页面的响应)
            for data in data_list:
                url = data['url']
                detail_data = self.get_data(url)
                # 从详情页面响应中抽取图片链接
                image_list = self.parse_detail_page(detail_data)
                # 下载图片
                self.download(image_list)
                # 翻页


if __name__ == '__main__':
    baidu = Baidu('炉石传说')
    baidu.run()
