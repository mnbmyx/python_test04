# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月26日 15:06
"""
import time
from time import sleep
import pytest
from baidu import base
from baidu.page.page import Page
from baidu.page import GetDriver
from baidu.common.url_yml import url_yml
from baidu.common.data_csv import data_csv

url = url_yml('../config/url.yml', 'bdfyurl', 'url')
data = data_csv('../data/data.csv')
cookice = url_yml('../config/url.yml','cookices','cookice')
@pytest.mark.parametrize(('content','note'), data)
class TestBaidu():
    @classmethod
    def setup_class(cls):
        # 打开百度翻译页面
        cls.driver = GetDriver.get_driver(url)
        cls.fy = Page(cls.driver)
        # 截图
        cls.fy.page_get_img()
        # 点击关闭弹窗
        cls.fy.page_click(loc=base.pop_btn)
        # 截图
        cls.fy.page_get_img()
        # 实现cookice登录百度账号
        cls.fy.page_cookice(cookice)

    @classmethod
    def teardown_class(cls):
        # 关闭浏览器
        GetDriver.quit_driver()

    def test_01_baidu(self,content,note):
        # 输入翻译内容
        self.fy.page_input(loc=base.input,key=content)
        # 点击翻译按钮
        self.fy.page_click(loc=base.fy_btn)
        sleep(1)
        # 输入笔记
        self.fy.page_input(loc=base.bj_input, key=note)
        # 点击收藏按钮
        self.fy.page_click(loc=base.bj_sc_btn)
        # 截图
        self.fy.page_get_img()
        if content==data[-1][0]:
            # 点击收藏夹
            self.fy.page_click(base.scj_btn)
            # 切换窗口
            self.fy.page_switch_windows()
            # 截图
            self.fy.page_get_img()

if __name__ == '__main__':
    pytest.main(['-s','test_baidu.py','--alluredir','../report/'])