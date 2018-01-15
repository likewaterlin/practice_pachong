# -*- coding: utf-8 -*-


import requests
import re

# 构建url
url = 'http://www.renren.com/923768535'

# 构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Cookie':'anonymid=jcg6icii-pjkehd; depovince=GW; jebecookies=1ce8841f-6133-4c27-9842-b6927eb03c77|||||; _r01_=1; ick_login=5553a389-c7f9-48d3-8c6e-2c759ab8effe; _de=4F1FF60C280AA48B2CD1201DB4C6DF4A; p=5bca05bcadc0b91733a981151fe188a25; first_login_flag=1; ln_uact=17173805860; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=722194d37675aa326418884b1bbc96ef5; societyguester=722194d37675aa326418884b1bbc96ef5; id=923768535; xnsid=638a195; loginfrom=syshome; ch_id=10016; JSESSIONID=abcH1uafxW-Inby21X5dw'
}
# 发送请求获取响应
response = requests.get(url,headers=headers)
# 验证是否登录成功
print(response.url)
with open('renren.html','wb') as f:
    f.write(response.content)

print(re.findall('迷途',response.content.decode()))