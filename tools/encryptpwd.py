# -*- coding:utf-8 -*-
'''
@Time       : 2020/9/3 18:44
@Author     : Joy
@FileName   : encryptpwd.py
@description: 将公钥加密成私钥,password 为登录密码
'''
import base64
import requests
import json,warnings
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from common import readfiles



def pwd_encryptwd(password='hzmcAdmin'):
        #TODO 解决路径在linux和mac上的处理
        #忽略异常
        warnings.filterwarnings('ignore')
        hostinfo = readfiles.read_yaml('interinfo/basic.yaml','mainhost')
        host = hostinfo.host
        url = 'https://' +host+ '/capaa/js/encrypt/encrypt.json'
        r = requests.get(url=url , verify=False)  # 获取公钥接口
        publickey = json.loads(r.text)['publicKey']
        publickey = b'-----BEGIN PUBLIC KEY-----\n' + bytes(publickey, 'utf8') + b'\n' + b'-----END PUBLIC KEY-----'
        raskey = RSA.importKey(publickey)
        cipher = PKCS1_v1_5.new(raskey)
        # cipher_text = base64.b64encode(cipher.encrypt(password))
        cipher_text = base64.b64encode(cipher.encrypt(bytes(password, 'utf8')))
        pravitekey = str(cipher_text, encoding='utf8').replace('+', '%2B')
        return pravitekey

if __name__ == '__main__':
    print(pwd_encryptwd())