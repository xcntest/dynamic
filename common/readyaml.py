# -*- coding:utf-8 -*-
'''
@Time       : 2020/6/28 19:03
@Author     : Joy
@FileName   : readyaml.py
'''

import yaml
import os

#读取yaml文件
def read_yaml(filepath,filename):
   #获取yaml文件路径
   yamlfile = os.path.join(filepath,filename)
   with open(yamlfile) as f:
       data = yaml.load(f, Loader=yaml.FullLoader)  # 从yaml读取
       return data  # 返回的是个字典


if __name__ == '__main__':
    #获取当前路径
    filePath = os.path.dirname(__file__)
    read_yaml()