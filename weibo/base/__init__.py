# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月27日 9:51
"""

from selenium.webdriver.common.by import By

"""
微博登录页面元素配置信息
"""

# 立即登录按钮
lj_login_btn = By.XPATH,'//*[@id="__sidebar"]/div/div[2]/div[1]/div/button'
# 账号登录按钮
zh_btn = By.XPATH,'//*[@id="app"]/div[5]/div[1]/div/div[2]/div/div/div[5]/a[1]'
# 账号输入框
zh_input = By.ID,'loginname'
# 密码输入框
paw_input = By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input'
# 登录按钮
login_btn = By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[6]/a'
# 错误用户名或密码提示
error_info = By.XPATH,'//div[3]/div[1]/p'
# 登录成功后的提示
login_info = By.XPATH,'//*[@id="qrTitle"]'


"""
微博首页页面元素配置信息
"""
# 输入内容文本框
wb_input = By.XPATH,'//*[@id="homeWrap"]/div[1]/div/div[1]/div/textarea'
# 发送微博按钮
wb_fs_btn = By.XPATH,'//*[@id="homeWrap"]/div[1]/div/div[4]/div/div[4]/button'
# 上传图片按钮
put_file_btn = By.XPATH,'//*[@id="homeWrap"]/div[1]/div/div[4]/div/div[1]/div/div[2]/div/span/div'
# 三个点按钮
other_btn = By.XPATH,'//*[@id="homeWrap"]/div[1]/div/div[4]/div/div[1]/div/div[6]/div/span/div'
# 点评按钮
dp_btn = By.XPATH,'//*[@id="homeWrap"]/div[1]/div/div[4]/div/div[1]/div/div[6]/div/div/div/div[2]'
# 点评搜索
dp_input = By.XPATH,'//*[@id="homeWrap"]/div[1]/div/div[5]/div[4]/div[1]/div/div[2]/div[1]/div/div/span/div/div/input'
# 搜索内容
sous_content = By.XPATH,'//*[@id="scroller"]/div[1]/div/div/div'
# 星星点评：五星
stars_btn = By.XPATH,'//*[@id="homeWrap"]/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div[1]/i[5]'