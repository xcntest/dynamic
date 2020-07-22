# -*- coding:utf-8 -*-
'''
@Time       : 2020/6/28 19:03
@Author     : Joy
@FileName   : readfiles.py
'''

import yaml
from pathlib import Path
#调试用，需删除
from tools import filetools


#读取yaml文件
def read_yaml(filepath):
    """
    :param filepath: 文件路径
    :return: 文件内容
    """
    #拼接根目录+文件子路径
    filename = Path.cwd().parent.joinpath(filepath)
    with open(filename) as f:
       data = yaml.load(f, Loader=yaml.FullLoader)
       return data  # 返回的是个字典





if __name__ == '__main__':
    #获取当前路径
    filePath = Path.cwd().parent.joinpath('sqlfiles/mysqlsql/DQL.yaml')
    print(filePath)
    data = read_yaml(filePath)
    print(data)
    # #字典访问
    # info = filetools.AttrDict(data['mysql'])
    # print(info.host,info.port,info.dbname,info.user,info.pwd)