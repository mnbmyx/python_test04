# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月26日 14:38
"""

from baidu.base.base import Base

"""
页面元素操作层
"""

class Page(Base):
    # 点击方法
    def page_click(self, loc):
        self.base_click(loc)

    # 获取value属性方法封装
    def page_get_value(self, loc):
        self.base_get_value(loc)

    # 输入方法
    def page_input(self, loc, key):
        self.base_input(loc,key)

    # 添加cookice
    def page_cookice(self,cookice):
        self.base_get_cookice(cookice)

    # 截图
    def page_get_img(self):
        self.base_get_img()

    # 切换窗口
    def page_switch_windows(self):
        self.base_switch_windows()