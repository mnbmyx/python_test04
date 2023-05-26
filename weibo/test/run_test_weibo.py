# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月27日 17:13
"""
# 导包
import pytest
# 运行测试文件并生成测试报告
pytest.main(['-s','test_weibo.py','--alluredir','../report/wb_report/'])