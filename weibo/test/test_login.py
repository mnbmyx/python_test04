# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月27日 10:49
"""
import time

import pytest
from weibo.page import GetDriver
from weibo.page.page import PageLogin
from weibo import base
from time import sleep
from weibo.common.data_csv import data_csv
from weibo.common.url_yml import url_yml

# 数据内容读取
login_url = url_yml('../config/url.yml', 'WBurl', 'url')
login_data = data_csv('../data/data.csv')
@pytest.mark.parametrize(('username','password','info'),login_data)
# 测试登录
class TestLogin():
    @classmethod
    def setup_class(cls):
        # 打开微博登录页面
        cls.driver = GetDriver.get_driver(login_url)
        cls.login = PageLogin(cls.driver)
        sleep(1)
        # 点击立即登录按钮
        cls.login.page_click(base.lj_login_btn)
        sleep(1)
        # 点击账号登录按钮
        cls.login.page_click(base.zh_btn)


    @classmethod
    def teardown_class(cls):
        # 关闭浏览器
        GetDriver.quit_driver()

    def test_login(self,username,password,info):
        # 切换窗口
        self.login.page_switch_windows()
        sleep(1)
        # 输入账号
        self.login.page_input(loc=base.zh_input,key=username)
        # 输入密码
        self.login.page_input(loc=base.paw_input,key=password)
        # 点击登录按钮
        self.login.page_click(base.login_btn)
        sleep(1)
        # 判断账号和密码是否正确
        if info == '登录验证':
            print('登录成功')
            assert self.login.page_info(base.login_info).text == info
        else:
            print(info)
            assert self.login.page_info(base.error_info).text == info
        # # 截屏
        self.login.page_get_img()

if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])
