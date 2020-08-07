# -*- coding:utf-8 -*-
'''
@Time       : 2020/8/7 13:55
@Author     : Joy
@FileName   : run.py.py
'''

import pytest
import os

case_path = os.path.join(os.getcwd())
#PATH = os.path.split(os.path.realpath(__file__))[0]

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './result/'])
    os.system("allure generate ./result/ -o ./allure-report/ --clean")
    os.system("allure open -h 127.0.0.1 -p 8883 ./allure-report/")

