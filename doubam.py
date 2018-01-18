# -*- coding: utf-8 -*-
# 目标 爬取电影影片list
import json

import requests


class Douban(object):
    def __init__(self):
        self.url = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?&start={}&count=50'
        self.n = 0
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36'
        }

        self.file = open('douban.json','w')

    def get_data(self,url):
        response = requests.get(url,headers=self.headers)
        return response.content.decode()

    def parse_data(self,data):
        # 将json字符串转换成字典
        dict_data = json.loads(data)
        # 获取电视剧数据列表
        tv_list = dict_data['subject_collection_items']
        # 构建存放数据用的列表
        result_list = list()
        # 遍历电视剧列表，从中拿出每一个电视剧的信息，进行数据抽取
        for tv in tv_list:
            temp = dict()
            temp['title'] = tv['title']
            temp['url'] = tv['url']
            temp['id'] = tv['id']
            temp['rating'] = tv['rating']
            result_list.append(temp)
        return result_list


    def save_data(self,data_list):
        for data in data_list:
            str_data = json.dumps(data,ensure_ascii=False) + ',\n'
            self.file.write(str_data)

    # 调用结束后会自动调用这个方法
    def __del__(self):
        self.file.close()

    def run(self):

        # 创建url
        # 创建headers
        # 提交请求和获取数据
        while True:
            url = self.url.format(self.n)
            # print(url)
            # 发送请求获取响应
            data = self.get_data(url)
            # 解析响应，获取目标数据
            # 分析数据
            data_list = self.parse_data(data)


            # 保存数据
            self.save_data(data_list)
            self.n+=50
            if len(data_list)is[]:
                break


if __name__ == '__main__':
    douban = Douban()
    douban.run()
