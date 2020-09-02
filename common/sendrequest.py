# -*- coding:utf-8 -*-
'''
@Time       : 2020/9/1 10:43
@Author     : Joy
@FileName   : sendrequest.py
'''

import json
import allure
import requests
import os
from common import readfiles,logger


class SendRequest:
    def __init__(self):
         self.session = requests.Session()

    #封装get请求
    def get_request(self,url,params=None,header=None):
        """
        get请求
        :param url: 请求URL
        :param params: 请求参数
        :param header: 请求头
        :return:
        """
        if not url.startwith('https//'):
            url = '%%s' % ('https://',url)














