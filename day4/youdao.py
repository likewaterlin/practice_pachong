# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-

# 这个网站我们需要爬走什么信息？翻译出来的信息
'''
提交的信息from data
i:love   ------输入的词
from:AUTO - ------固定自动
to:AUTO  ----------固定自动
smartresult:dict
client:fanyideskweb
salt:1516271550069
sign:a210b25fe84de4234145a3229d8e51ac
doctype:json
version:2.1
keyfrom:fanyi.web
action:FY_BY_REALTIME
typoResult:false

i: n,
from: _, -----_ = "AUTO"
to: C,  -------C = "AUTO"
smartresult: "dict",
client: E,   ------E = "fanyideskweb"
salt: r,  -----"" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
sign: o, ----u.md5(E + n + r + O)
doctype: "json",
version: "2.1",
keyfrom: "fanyi.web",
action: "FY_BY_DEFAULT",
typoResult:false

'''
import hashlib
import json
import random

import re
import requests
import time


class Youdao(object):
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'Cookie': 'DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=-590609486@101.81.189.4; JSESSIONID=abczwLo7W7q0W5KIQ0iew; OUTFOX_SEARCH_USER_ID_NCOO=414878122.4614757; fanyi-ad-id=39535; fanyi-ad-closed=1; ___rl__test__cookies=1516271550058',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Referer': 'http: // fanyi.youdao.com /',
        }
        self.post_data = None

    def generate_post_data(self, word):
        now = time.time()
        timestamp = re.match('(\d+).(\d+)', str(now))
        tempstr = timestamp.group(1) + timestamp.group(2)
        tempstr = tempstr[0:13]
        randomint = random.randint(0, 9)
        salt = str(int(tempstr) + randomint)
        E = "fanyideskweb"
        n = word
        r = salt
        O = "aNPG!!u6sesA>hBAW1@(-"
        md5str = E + n + r + O

        # 创建hash对象
        md5 = hashlib.md5()

        # 填充数据
        md5.update(md5str.encode())

        # 获取hash值
        sign = md5.hexdigest()

        self.post_data = {
            'i': word,
            'from': 'AUTO',  # -----_ = "AUTO"',
            'to': 'AUTO',  # -------C = "AUTO"',
            'smartresult': 'dict',
            'client': 'fanyideskweb',  # ------E = "fanyideskweb"',
            'salt': salt,  # -----"" + ((newDate).getTime() + parseInt(10 * Math.random(), 10))',
            'sign': sign,  # ----u.md5(E + n + r + O)',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_DEFAULT',
            'typoResult': False,
        }

    def get_data(self):
        response = requests.post(self.url, headers=self.headers, data=self.post_data)
        return response.content.decode()

    def parse_data(self, data):
        json_data = json.loads(data)
        result = json_data['translateResult'][0][0]['tgt']
        print(result)

    def run(self):
        # 创建url
        # 创建请求头
        # 构造post数据
        self.generate_post_data('我心永恒')
        # 发送请求接受数据
        data = self.get_data()
        # 解析响应抽取数据
        self.parse_data(data)


if __name__ == '__main__':
    youdao = Youdao()
    youdao.run()
