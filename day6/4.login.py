# -*- coding: utf-8 -*-

from selenium import webdriver
import pytesseract
from PIL import Image
import requests

url = 'https://accounts.douban.com/login'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

dr = webdriver.Chrome()

dr.get(url)

# 定位账号
el_user = dr.find_element_by_id('email')
el_user.send_keys('m17173805860@163.com')

# 定位密码
el_user = dr.find_element_by_id('password')
el_user.send_keys('1qaz@WSX3edc')

try:
    # 定位验证码模块输入框
    el_captcha_input = dr.find_element_by_id('captcha_field')
    el_captcha = dr.find_element_by_id('captcha_image')
    captcha_url = el_captcha.get_attribute('src')
    print(captcha_url)

    data = requests.get(captcha_url,headres = headers).content
    with open('temp.jpg','wb')as f:
        f.write(data)

    im = Image.open('temp.jpg')
    captcha = pytesseract.image_to_string(im)
    print('--',captcha,'--')

    # 输入验证码
    el_captcha_input.send_keys(captcha)
except:


    # 定位提交按钮元素
    el_user = dr.find_element_by_name('login')
    el_user.click()








