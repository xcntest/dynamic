# -*- coding:utf-8 -*-
'''
@Time       : 2020/8/31 14:40
@Author     : Joy
@FileName   : conftest.py
'''

import pytest
import requests
import os
from common import  logger,readfiles
import pytest

@pytest.fixture(scope="session")
def login(request):
    log = logger.Log()
    url = "https://192.168.51.126/capaa/j_spring_security_check"

}


