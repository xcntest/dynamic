# -*- coding:utf-8 -*-
'''
@Time       : 2020/8/3 14:36
@Author     : Joy
@FileName   : makedir.py
'''
import os

def mk_dir(path):
    if not os.path.exists(path):
        try:
            #如果不存在则创建目录
            os.makedirs(path)
        except Exception as e:
            print(e)





if __name__ == '__main__':
    dir = '/Users/xiongting/Desktop/Mask_Scripts/dynamic/Logs'
    mk_dir(dir)




