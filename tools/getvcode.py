import tesserocr
from PIL import Image

image = Image.open('test.png')

image.show()  # ���Դ�ӡ��ͼƬ����Ԥ��
print(tesserocr.image_to_text(image))