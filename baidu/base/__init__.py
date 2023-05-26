# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月26日 14:10
"""

from selenium.webdriver.common.by import By

# __all__=['input','fy_btn','qh_btn','collect_btn']

# # url地址
# url = 'https://fanyi.baidu.com/'
# 弹窗关闭按钮
pop_btn = By.XPATH,'//*[@id="app-guide"]/div/div/div[2]/span'
# 文本输入框
input = By.ID,'baidu_translate_input'
# 翻译按钮
fy_btn = By.ID,'translate-button'
# 切换按钮
qh_btn = By.XPATH,'//*[@id="main-outer"]/div/div/div[1]/div[1]/div[1]/a[2]/span'
# 收藏夹按钮
scj_btn = By.XPATH,'//*[@id="main-outer"]/div/div/div[1]/div[1]/div[4]/a[1]/span'
# 笔记按钮
bj_btn = By.XPATH,'//*[@id="main-outer"]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/a[4]'
# 笔记输入框
bj_input = By.XPATH,'//*[@id="noteContainer"]/div/div[1]/div[1]/textarea'
# # 笔记输入
# bj_key = '这是做实验时做的笔记'
# 笔记收藏夹按钮
bj_sc_btn = By.XPATH,'//*[@id="noteContainer"]/div/div[2]/a'
# 文本输入框输入的值
# key = 'spider'