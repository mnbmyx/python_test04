# -*- coding:utf-8 -*-
"""
作者：myx
日期：2023年05月26日 18:06
"""

import yaml

'''
通过传递文件名，section和key，取yml文件中的内容
'''
def url_yml(file, section, key):
    with open(file, 'r', encoding='utf8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data[section][key]

if __name__ == '__main__':
    value = url_yml('../config/url.yml', 'bdfyurl', 'url')
    print(value)
