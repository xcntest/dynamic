# -*- coding:utf-8 -*-
'''
@Time       : 2020/6/28 19:03
@Author     : Joy
@FileName   : readfiles.py
'''

import yaml
from pathlib import Path
from tools import filetools
from common import logger


#读取yaml文件
def read_yaml(filepath,section:str):
    """
    :param filepath: 文件路径
    :return: 文件内容
    """
    #拼接根目录+文件子路径
    loger = logger.Log()
    #TODO 这里要修改一下读取方式
    #运行main为run.py
    filename = Path.cwd().joinpath(filepath)
    #运行main为非run.py
    #filename = Path.cwd().parent.joinpath(filepath)

    if not Path.exists(filename):
        loger.error("文件不存在")

    with open(filename,encoding='utf-8') as f:
       data = yaml.load(f)
       try:
            yamlinfo = filetools.AttrDict(data[section])
       except Exception as e:
            print(e)
            loger.error('传入的section错误，传入值为{}'.format(e))
    return yamlinfo # 返回的是个AttrDict字典



if __name__ == '__main__':
    #获取当前路径
    filePath = Path.cwd().parent.joinpath('interinfo/login.yaml')
    print(filePath)
    data = read_yaml(filePath,'login')
    print(type(data.data))
