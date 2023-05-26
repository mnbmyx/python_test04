# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月27日 15:18
"""
import time
import pytest
from weibo.page import GetOptions
from weibo.page.page import PageLogin
from weibo import base
from time import sleep
from weibo.common.data_csv import data_csv
from weibo.common.url_yml import url_yml

# 数据内容读取
login_url = url_yml('../config/url.yml', 'WBurl', 'url')
login_data = data_csv('../data/data.csv')
cookice = '../data/cookie.json'
service = url_yml('../config/url.yml', 'Service', 'service')
contents = data_csv('../data/content.csv')

@pytest.mark.parametrize(('content','filepath'),contents)
# 测试发布微博
class TestWeibo():
    @classmethod
    def setup_class(cls):
        cls.driver = GetOptions.get_driver(login_url,cookice,service)
        cls.wb = PageLogin(cls.driver)
        cls.wb.page_get_img()

    @classmethod
    def teardown_class(cls):
        # 关闭浏览器
        GetOptions.quit_driver()

    def test_01_input(self,content,filepath):
        # 输入内容
        self.wb.page_input(base.wb_input,content)
        if content == contents[-2][0] or content == contents[-1][0]:
            # 点击三个点
            self.wb.page_click(base.other_btn)
            # 点击点评按钮
            self.wb.page_click(base.dp_btn)
            # 输入内容
            self.wb.page_input(base.dp_input,content)
            # 点击搜索的内容
            self.wb.page_click(base.sous_content)
            # 点五星
            self.wb.page_click(base.stars_btn)
        self.wb.page_click(base.put_file_btn)
        sleep(1)
        self.wb.page_putfile(filepath)
        sleep(2)
        self.wb.page_get_img()
        self.wb.page_click(base.wb_fs_btn)
        self.wb.page_get_img()

if __name__ == '__main__':
    pytest.main(['-s','test_weibo.py'])