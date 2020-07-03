# -*- coding:utf-8 -*-
'''
@Time       : 2020/6/30 19:35
@Author     : Joy
@FileName   : dbconnect.py
'''

import pymysql
from common import tools,readyaml
import os

# 获取当前路径
filePath = os.path.dirname(__file__)
data = readyaml.read_yaml(filePath, 'config.yaml')

#获取连接
def connectdb(dbtype):
    """
    :param dbtype: db的类型名，'mysql'
    :return:
    """
    # 获取当前路径
    filePath = os.path.dirname(__file__)
    data = readyaml.read_yaml(filePath, 'config.yaml')

    info = tools.AttrDict(data[dbtype])
    conn = pymysql.connect(
                            host = info.host,
                            port = info.port,
                            db = info.dbname,
                            user = info.user,
                            passwd = info.pwd,
                            charset = 'utf8')

    return conn


def quey_db(sql):


    # with conn as cursor:
    #      with cursor:




if __name__ == '__main__':
    print(data)



