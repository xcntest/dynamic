# -*- coding:utf-8 -*-
'''
@Time       : 2020/9/3 09:56
@Author     : Joy
@FileName   : getvcode.py
@description :https://www.cnblogs.com/jiahm/p/13539185.html（百度识别图片接口）
'''
#
import requests
import os
from PIL import Image
from io import BytesIO
from aip import AipOcr
from tools import makedir
from common import logger


class GetVcode:
    def __init__(self):
        self.dir = os.path.join(os.path.split(os.path.dirname(__file__))[0],'images')
        #获取图片接口
        self.url = 'https://192.168.230.121/capaa/v1/user/verification/image'
        self.log = logger.Log()


    #获取验证码图片
    def get_pictures(self):
        makedir.mk_dir(self.dir)
        response = requests.get(self.url, verify=False)
        oriimage = Image.open(BytesIO(response.content))
        #对图片转化为灰度图像
        img = oriimage.convert('L')
        # # pixdata = img.load()
        # # w, h = img.size
        # threshold = 155# 该阈值不适合所有验证码，具体阈值请根据验证码情况设置
        # table = []
        # for i in range(256):
        #     if i< threshold:
        #         table.append(0)
        #     else:
        #         table.append(1)
        # img = img.point(table,'1')
        # # 遍历所有像素，大于阈值的为黑色
        # for y in range(h):
        #     for x in range(w):
        #         if pixdata[x, y] < threshold:
        #             pixdata[x, y] = 0
        #         else:
        #             pixdata[x, y] = 255
        # #删除扰乱识别的像素点
        # data = img.getdata()
        # w, h = img.size
        # black_point = 0
        # for x in range(1, w - 1):
        #     for y in range(1, h - 1):
        #         mid_pixel = data[w * y + x]  # 中央像素点像素值
        #         if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
        #             top_pixel = data[w * (y - 1) + x]
        #             left_pixel = data[w * y + (x - 1)]
        #             down_pixel = data[w * (y + 1) + x]
        #             right_pixel = data[w * y + (x + 1)]
        #             # 判断上下左右的黑色像素点总个数
        #             if top_pixel < 10:
        #                 black_point += 1
        #             if left_pixel < 10:
        #                 black_point += 1
        #             if down_pixel < 10:
        #                 black_point += 1
        #             if right_pixel < 10:
        #                 black_point += 1
        #             if black_point < 1:
        #                 img.putpixel((x, y), 255)
        #             black_point = 0
        img.save(self.dir + '/' + 'vcode.png')
        pigpath = os.path.join(self.dir,'vcode.png')
        return pigpath

    #获取验证码
    def baiduOCR(self):  # picfile:图片文件名
        # 百度提供
        """ 你的 APPID AK SK """
        # 应用的appid
        APP_ID = '22532565'
        # 应用的appkey
        API_KEY = 'fCvsC8UOdrLFPDGFPpQW0X1I'
        # 应用的secretkey
        SECRET_KEY = 'oMnORbkMcdnTnEm2XNPzls08jOxGEGkx'
        picfile = self.get_pictures()
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        i = open(picfile, 'rb')
        img = i.read()
        """ 调用通用文字识别（高精度版） """
        message = client.basicAccurate(img)
        #message={'log_id': 101386452554647523, 'words_result_num': 1, 'words_result': [{'words': ' PHED'}]}
        i.close()
        try:
            vcode = message.get('words_result')[0].get('words')
            return vcode
        except Exception as e:
            self.log.debug("未获取到有效验证码{}:{}".format(message,e))





if __name__ == '__main__':
   # baiduOCR('C:/test.png')
   #  baiduOCR('/Users/xiongting/Desktop/20190527112233258.png')
   a = GetVcode()
   print(type(a.baiduOCR()))



