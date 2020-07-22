# -*- coding:utf-8 -*-
'''
@Time       : 2020/7/4 11:50
@Author     : Joy
@FileName   : test.py
'''

from pathlib import Path


# #p = Path('/Users/xiongting/Desktop/Mask_Scripts/dynamic/common/test.py')#当前路径
# p = Path.cwd().parent#当前路径
# print(p.cwd().parent)
# print(p.home())
#
# p3 = p.joinpath('sqlfiles/mysqlsql/DQL.yaml')
# print(p3)


import  datetime

now = '2017-2-1 13:12:34'
a = isinstance(now,datetime.time)
print(a)
