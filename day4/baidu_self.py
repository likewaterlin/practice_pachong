# -*- coding: utf-8 -*-


# 这个网站我们需要爬走什么信息？title?url?image?text?或者其他的什么信息
import os

from lxml import etree

import requests


class Baidu(object):
    def __init__(self, name):
        # 初始值除了url headers还需要哪些数据？headers的过新或者过旧是否导致数据下载或者获取有问题？
        self.url = 'https://tieba.baidu.com/f?ie=utf-8&kw={}'.format(name)

        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'
        }

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
        # //*[@id="thread_list"]/li[2]/div/div[2]/div[1]/div[1]/a
        data_list = html.xpath('//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')

        data_dict = list()

        for data in data_list:
            temp = dict()
            temp['url'] = 'https://tieba.baidu.com' + data.xpath('./@href')[0]
            temp['content'] = data.xpath('text()')[0]
            data_dict.append(temp)
        print(data_dict)

        # next_url = html.xpath('//*[@id="frs_list_pager"]/a[@class="next pagination-item"]')  仅仅指向下一页，并不是有效的链接
        next_node = html.xpath('//*[@id="frs_list_pager"]/a[last()-1]/@href')
        next_url = 'http:' + next_node[0] if len(next_node) > 0 else None

        print(next_url)
        return data_dict, next_url

        # return data_dict

    # 下载图片要的链接

    def image_url(self, data):
        html = etree.HTML(data)

        image_url_list = html.xpath('//cc/div[contains(@id,"post_content_")]/img/@src')

        return image_url_list

    def download(self, image_url_list):
        # 下载数据，如何执行？
        # download 的语句是和保存差不多 但是在下载之前需要判断哪些数据是要放在哪里，如果没有文件夹该怎么办？
        # 判断参照如下
        # if not os.path.exists('image'):
        #  os.makedirs('image')
        if not os.path.exists('image'):
            os.makedirs('image')
        for images in image_url_list:
            # 此句需斟酌
            file_name = 'image' + os.sep + images.split('/')[-1]
            data = self.get_data(images)

            with open(file_name, 'wb')as f:
                f.write(data)

    def run(self):
        # 创建url
        # 创建请求头
        # 发送请求接受数据
        next_url = self.url
        while next_url:
            data = self.get_data(next_url)
            # 解析数据  解析有很多种，需要分析爬下来的信息的类型
            data_dict, next_url = self.parse_data(data)

            # 下载数据,下的是什么数据？需要什么条件才能进行下载呢，是链接 呢 ？
            # 这个for循环有点乱
            for data in data_dict:
                url = data['url']
                detail_data = self.get_data(url)
                image_url_list = self.image_url(detail_data)

                self.download(image_url_list)

                # 在最后看看是否需要重复爬取数据呢？


if __name__ == '__main__':
    baidu = Baidu('炉石传说')
    baidu.run()
