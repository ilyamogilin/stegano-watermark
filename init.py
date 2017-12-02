#!/usr/local/bin/python3

from factory import ImageFactory

factory = ImageFactory()
img = factory.createImage("images/map.bmp")
key = img.encrypt("10100001")
img.write()
new_img = factory.createImage("images/new_map.bmp")
message = new_img.decrypt(key)
print(message)
# print(img.decrypt(img.encrypt("101000010100101010010100110010101010101010101111111100001010101010")))