# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月26日 15:06
"""
from time import sleep
import pytest
from baidu import base
from baidu.page.page import PageBaidu
from baidu.page import GetDriver
from parameterized import parameterized
from baidu.common.url_yml import url_yml
from baidu.common.data_csv import data_csv

url = url_yml('../config/url.yml', 'bdfyurl', 'url')
data = data_csv('../data/data.csv')

@pytest.mark.parametrize(('content','note'), data)

class TestBaidu():
    @classmethod
    def setup_class(cls):
        cls.driver = GetDriver.get_driver(url)
        cls.fy = PageBaidu(cls.driver)
        sleep(1)
        # 点击关闭弹窗
        cls.fy.page_bd_click(loc=base.pop_btn)
        sleep(1)
        # 实现cookice登录百度账号
        cls.fy.page_get_cookice()
        sleep(1)


    @classmethod
    def teardown_class(cls):
        GetDriver.quit_driver()


    def test_01_baidu(self,content,note):
        # 输入翻译内容
        self.fy.page_bd_input(loc=base.input,key=content)
        sleep(1)
        # 点击翻译按钮
        self.fy.page_bd_fy(loc=base.fy_btn)
        sleep(1)
        # 点击笔记按钮
        # self.fy.page_bd_click(loc=base.bj_btn)
        sleep(1)
        # 输入笔记
        self.fy.page_bd_input(loc=base.bj_input, key=note)
        sleep(1)
        # 点击收藏按钮
        self.fy.page_bd_click(loc=base.bj_sc_btn)
        sleep(1)


if __name__ == '__main__':
    pytest.main(['-s','test_baidu.py'])