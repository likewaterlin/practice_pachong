#coding:utf-8
from selenium import webdriver
import time
url = 'https://qzone.qq.com/'

# 构建浏览器对象
dr = webdriver.Chrome()

# 访问url
dr.get(url)

# 进入框架的两种方式
# 通过id
# dr.switch_to.frame('login_frame')
# 通过元素定位
el_1 = dr.find_element_by_xpath('//*[@id="login_frame"]')
dr.switch_to.frame(el_1)

# 尝试点击账号密码登录按钮
el = dr.find_element_by_id('switcher_plogin')
el.click()

# 输入账号密码
el_user = dr.find_element_by_id('u')
el_user.send_keys('2634809316')
el_pwd = dr.find_element_by_id('p')
el_pwd.send_keys('461324karura')
time.sleep(2)
# 点击登录
el_sub = dr.find_element_by_id('login_button')
el_sub.click()