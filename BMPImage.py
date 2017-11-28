#!/usr/local/bin/python3

from image import Image
import struct
import math

class BMPImage(Image):
    """BMPImage Class"""
    def __init__(self, name, key, message):
        super(BMPImage, self).__init__(self, name, key, message)

        # Opening file
        with open(name, 'rb') as f:
            data = bytearray(f.read())

        self.name = name
        self.key = key
        self.messge = message

        # Parsing BMP header
        self.type = data[0:2].decode() # Type
        self.size = struct.unpack_from('I', data, 2)[0] # the size of the BMP file in bytes
        self.res1 = struct.unpack_from('H', data, 6)[0] # reserved; actual value depends on the application that creates the image
        self.res2 = struct.unpack_from('H', data, 8)[0] # reserved; actual value depends on the application that creates the image
        self.offset = struct.unpack_from('I', data, 10)[0] # the offset, i.e. starting address, of the byte where the bitmap image data (pixel array) can be found.

        # Parsing DIB header
        # Support only for BITMAPINFOHEADER and BI_RGB compression method (no compression)
        # TODO: add support for BI_BITFIELDS
        self.dib_header_size = struct.unpack_from('I', data, 14)[0] # The size of DIB header
        self.width = struct.unpack_from('i', data, 18)[0] # the bitmap width in pixels (signed integer)
        self.height = struct.unpack_from('i', data, 22)[0] # the bitmap height in pixels (signed integer)
        self.color_planes = struct.unpack_from('H', data, 26)[0] # the number of color planes (must be 1)
        self.bpp = struct.unpack_from('H', data, 28)[0] # the number of bits per pixel, which is the color depth of the image. Typical values are 1, 4, 8, 16, 24 and 32.
        self.compression = struct.unpack_from('I', data, 30)[0] # the compression method being used. See the next table for a list of possible values
        self.bm_size = struct.unpack_from('I', data, 34)[0] # the image size. This is the size of the raw bitmap data; a dummy 0 can be given for BI_RGB bitmaps.
        self.hor_res = struct.unpack_from('i', data, 38)[0] # the horizontal resolution of the image. (pixel per metre, signed integer)
        self.ver_res = struct.unpack_from('i', data, 42)[0] # the vertical resolution of the image. (pixel per metre, signed integer)
        self.num_of_colors = struct.unpack_from('I', data, 46)[0] # the number of colors in the color palette, or 0 to default to 2^n
        self.imp_colors = struct.unpack_from('I', data, 50)[0] # the number of important colors used, or 0 when every color is important; generally ignored

        # Image array
        bpp = self.bpp
        width = self.width
        height = self.height
        offset = self.offset
        row_size = math.floor(float(bpp * width + 31) / 32) * 4 # TODO: move to class' field?
        padding = row_size % int(bpp / 8 * width) # TODO: move to class' field?

        self.img_data = [[[0 for i in range(3)] for j in range(height)] for k in range(width)]

        pointer = offset
        for j in range(height):
            for i in range(width):
                print('OK', i, j)
                for k in range(3):
                    self.img_data[i][j][k] = struct.unpack_from('B', data, pointer + k)[0]
                pointer += 3
            pointer += padding
        print(img_data)

    def getImageArray():
        # Refactors self.array field for algorithm module
        pass

    def setImageArray(img_data):
        # Refactors back img_data to normal (original) state
        pass

    def write():
        # Writes all fields to file
        pass

img = Image('image.bmp', '', '')
