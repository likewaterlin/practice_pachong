# -*- coding: utf-8 -*-

'''
<a target="_blank" class="image share_url" href="http://neihanshequ.com/p74232017685/" data-group-id="74232017685" >

			<div class="upload-txt  no-mb">
				<h1 class="title">
				<p>💍不管你有多么真诚，遇到怀疑你的人，你就是谎言；不管你有多么单纯，遇到复杂的人，你就是有心计；不管你有多么天真，遇到现实的人，你就是笑话，不管你多么专业，遇到不懂的人，你就是空白。所以，不要太在乎别人对你的评价，你需要的只是做最好的自己。</p>
				</h1>

'''
import json
import re
import requests


class Neihan(object):

    def __init__(self):
        self.url = 'http://neihanshequ.com/'
        self.ajax_url = 'http://neihanshequ.com/joke/'
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        self.file = open('neihan.json','w')

    def get_data(self,url,param=None,headers=None):
        if param is None:
            response = requests.get(url,headers=self.headers)
        else:

            response = requests.get(url,headers=self.headers,params=param)


        return response.content.decode()

    def parse_first_data(self,data):
        result_list = re.findall('<a target="_blank" class="image share_url" href="(.*?)".*?<p>(.*?)</p>',data,re.S)
        data_list = list()
        for result in result_list:
            temp = {}
            temp['link'] = result[0]
            temp['content'] = result[-1]
            data_list.append(temp)


        max_time = re.findall("max_time: '(\d+)'", data)[0]

        return data_list, max_time


    def save_data(self,data_list):
        for data in data_list:
            str_data = json.dumps(data,ensure_ascii=False)+ ',\n'
            self.file.write(str_data)

    def __del__(self):
        self.file.close()

    def parse_ajax_data(self,ajax_data):
        dict_data = json.loads(ajax_data)

        result_list = dict_data['data']['data']

        data_list = list()

        for data in result_list:
            temp =dict()
            temp['link'] = data['group']['share_url']
            temp['content']=data['group']['content']
            data_list.append(temp)

        max_time = dict_data['data']['max_time']
        return data_list,max_time


    def run(self):


        # 创建url
        # 创建headers
        # 发送请求接受数据
        data = self.get_data(self.url)

        # 解析数据
        data_list,max_time = self.parse_first_data(data)

        # 保存数据
        self.save_data(data_list)

        while True:
            data = {
                "is_json": "1",
                "app_name": "neihanshequ_web",
                "max_time": max_time
            }

            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                'Cookie': 'csrftoken=d3e1c00d039382589aa034f0659ab7a2; tt_webid=6510495316730594820; uuid="w:fd73fc31c1de4dc0a2455f8233fd496b"; _ga=GA1.2.674352354.1515842819; _gid=GA1.2.1410837842.1516091543; _gat=1',
                'Referer': 'http://neihanshequ.com/'
            }
            ajax_data = self.get_data(self.ajax_url,data,headers)

            data_list,max_time = self.parse_ajax_data(ajax_data)
            self.save_data(data_list)
            if len(data_list) is 0:
                break



if __name__ == '__main__':
    neihan = Neihan()
    neihan.run()
