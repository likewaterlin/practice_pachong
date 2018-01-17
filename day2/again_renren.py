# -*- coding: utf-8 -*-

# 构建url
# 构建header
# 发送和接收请求数据
# 保存数据
import re
import requests


class Renren(object):
    def __init__(self):
        self.url = 'http://www.renren.com/PLogin.do'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0',
        }
        self.session = requests.session()
        self.post_data = {
            "email": "17173805860",
            "password": "1qaz@WSX3edc",
        }

    def get_data(self):
        response = self.session.post(self.url, data=self.post_data, headers=self.headers)
        print(re.findall('迷途', response.content.decode()))
        return response.content



    def save_data(self, data):
        with open('renren1.html', 'wb')as f:
            f.write(data)


    def run(self):
        data1 = self.get_data()
        self.save_data(data1)



if __name__ == '__main__':
    renren = Renren()
    renren.run()

#
# import re
# import requests
#
# url = 'http://www.renren.com/PLogin.do'
#
# headers ={
#           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'
# }
#
# post_data ={
#     "email": "17173805860",
#     "password": "1qaz@WSX3edc",
# }
# # 实例化session对象  为什么？作用是什么在这段代码里面
# session=requests.session()
#
# # 发送请求获取响应
# session.post(url,headers=headers,data=post_data)
#
# # 验证登陆
#
# response=  session.get('http://www.renren.com/923768535')
# print(re.findall('迷途',response.content.decode()))
#
