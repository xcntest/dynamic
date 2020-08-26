import tesserocr
from PIL import Image

image = Image.open('test.png')

image.show()  # 可以打印出图片，供预览
print(tesserocr.image_to_text(image))