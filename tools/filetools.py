# -*- coding:utf-8 -*-
'''
@Time       : 2020/6/30 19:02
@Author     : Joy
@FileName   : filetools.py
'''


#字典属性化访问,获取字典内的信息时
class AttrDict:
    def __init__(self,d:dict):
        self.__dict__.update(d if isinstance(d,dict) else {})

    def __setattr__(self, key, value):
        #允许修改属性
        raise NotImplementedError

   # TODO:复习一下repr魔术方法
    def __repr__(self):
        return "<AttrDict {}>".format(self.__dict__)


    def __len__(self):
        return len(self.__dict__)


if __name__ == '__main__':
    d = {'mysql':{'host':'192.168.51.126'}}
    a = AttrDict(d['mysql'])
    print(a.host)
