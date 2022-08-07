import os, sys
from PIL import Image, ImageFilter

i = Image.open('image.jpg')

# i.show()

with i as image:
    width = round(image.size[0] * 0.2)
    height = round(image.size[1] * 0.2)
    f = image.resize((width, height), Image.BICUBIC)
    l = f.filter(ImageFilter.SHARPEN)
    l.save('3.jpg', optimize=True, quality=95, progressive=True)

i2 = Image.open('3.jpg')
# i2.show()


i_size = os.stat('image.jpg')
i2_size = os.stat('3.jpg')
size = i_size.st_size / 1024 / 1024
size2 = i2_size.st_size / 1024 / 1024

print(i.size, i.format, f'{round(size, 2)} MB')
print(i2.size, i2.format, f'{round(size2, 2)} MB')