#!/usr/local/bin/python3

from factory import ImageFactory

factory = ImageFactory()
img = factory.createImage("images/image.bmp", "some_key", "some_message")
data = img.getImageArray()
data[1][1] = [100, 123, 203]
img.setImageArray(data)
img.write()
