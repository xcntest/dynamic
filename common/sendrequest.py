# -*- coding:utf-8 -*-
'''
@Time       : 2020/9/1 10:43
@Author     : Joy
@FileName   : sendrequest.py
'''

import allure
import requests
from common import logger



class SendRequest(object):
    def __init__(self):
         self.log = logger.Log()

    #封装get请求
    def get_request(self,url,params=None,header=None,**kwargs):
        """
        get请求
        :param url: 请求URL
        :param params: 请求参数
        :param header: 请求头
        :return:
        """
        if not url.startwith('https//'):
            url = "https://"+url
        with allure.step("GET请求接口"):
            allure.attach("请求地址为:",url)
        try:
            #**kwargs这里这样写的话，需要传值用关键字参数,如:cookies=
            response = requests.get(url=url,params=params,headers=header, **kwargs)
        except requests.RequestException as e:
             self.log.debug("Exception{} url{}".format(e,url))
        except Exception as e:
            self.log.debug(e)
        #TODO 对resopnse返回内容进行处理
        return response


    def post_request(self,url,data,header=None,**kwargs):
        if 'application/x-www-form-urlencoded' in header['content-Type']:
            try:
                response = requests.post(url=url,data=data,headers=header,**kwargs)
            except requests.exceptions.RequestException as e:
                self.log.debug("Exception {} url {}".format(e.url))
            except Exception as e:
                self.log.info(e)
        elif'application/json' in header['content-Type']:
            try:
                response = requests.post(url=url,json=data,headers=header,**kwargs)
            except requests.exceptions.RequestException as e:
                self.log.debug("Exception {} url {}".format(e.url))
            except Exception as e:
                self.log.info(e)
        return response































