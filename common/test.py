import requests
from PIL import Image
from io import BytesIO
import os
from tools import getvcode


res = requests.get(url='https://192.168.230.121/capaa/v1/user/verification/image',verify=False)
image = Image.open(BytesIO(res.content))
image.save('vcode.jpeg')
getvcode.GetVcode().baiduOCR('vcode.jpeg')


