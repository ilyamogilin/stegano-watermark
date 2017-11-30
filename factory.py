#!/usr/local/bin/python3

from image import Image
from BMPImage import BMPImage
from misc import *

class ImageFactory(object):
    """Factory for Image abstract class"""
    def __init__(self):
        super(ImageFactory, self).__init__()

    def createImage(self, filename):
        # Creates a class of necessery type
        ext = getExtension(filename)
        if ext == 'bmp':
            return BMPImage(filename)
