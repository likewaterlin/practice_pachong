

#coding:utf-8
import requests
from lxml import etree
import os

class Baidu(object):

    def __init__(self, name):
        self.url = 'http://tieba.baidu.com/f?kw={}'.format(name)
        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'
        }

    def get_data(self, url):
        response = requests.get(url,headers=self.headers)
        return response.content

    def parse_list_page(self, data):
        # with open('baidu.html','wb')as f:
        #     f.write(data)
        # 将html源码转换成element对象
        html = etree.HTML(data)

        # 获取详情页面的节点列表
        node_list = html.xpath('//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')
        print(node_list)
        data_list = list()
        # 遍历所有的节点列表
        for node in node_list:
            # 提取数据
            temp = dict()

            temp['url'] = 'http://tieba.baidu.com' + node.xpath('./@href')[0]
            temp['title'] = node.xpath('./text()')[0]
            print(temp)
            data_list.append(temp)

        # 提取下一页链接
        next_node = html.xpath('//*[@id="frs_list_pager"]/a[last()-1]/@href')
        next_url = 'http:' + next_node[0] if len(next_node) > 0 else None

        return data_list, next_url

    def parse_detail_page(self, data):
        # 创建element对象
        html = etree.HTML(data)

        # 提取图片链接
        image_list = html.xpath("//cc/div[contains(@id,'post_content_')]/img/@src")
        # print(image_list)
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
        # 构建url
        # 构建请求头

        next_url = self.url

        # while next_url:
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
    baidu = Baidu('旅行吧')
    baidu.run()