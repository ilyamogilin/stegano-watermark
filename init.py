#!/usr/local/bin/python3

from factory import ImageFactory

factory = ImageFactory()
img = factory.createImage("images/image1.bmp")
img.encrypt("1010")
img.write()
