# -*- coding:utf-8 -*-
'''
@Time       : 2020/8/31 14:40
@Author     : Joy
@FileName   : conftest.py
'''

import pytest
import requests
from common import readfiles,logger
from tools import getvcode,encryptpwd

@pytest.fixture(scope="session")
def  send2session():
      s = requests.Session()
      log = logger.Log()
      loginfo = readfiles.read_yaml('interinfo/login.yaml','login')
      host = readfiles.read_yaml('interinfo/basic.yaml','mainhost').host
      password = encryptpwd.pwd_encryptwd(loginfo.data['j_password'])
      loginfo.data['j_password'] = password
      vcode = getvcode.GetVcode().baiduOCR()
      url = 'https://' +host+loginfo.url
      #TODO 这个循环逻辑好像有点问题，完成后尝试优化
      while True:
            while vcode is None or len(vcode)<4:
                  vcode = getvcode.GetVcode().baiduOCR()
            else:
                  loginfo.data['verCode'] = vcode
                  response = s.post(url=url,data=loginfo.data,headers=loginfo.headers,verify=False)
                  log.info(loginfo.data)
                  if response.status_code == 200:
                        print(response.status_code)
                        return s
                        break




send2session()






