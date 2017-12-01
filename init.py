#!/usr/local/bin/python3

from factory import ImageFactory

factory = ImageFactory()
img = factory.createImage("images/map.bmp")
img.encrypt("101000010100101010010100110010101010101010101111111100001010101010")
img.write()
