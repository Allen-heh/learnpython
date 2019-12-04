from PIL import Image

image = Image.open('/opt/heh/d14/pic/141_1498.jpg')
print(image.format, image.size, image.mode)
#image.show()
