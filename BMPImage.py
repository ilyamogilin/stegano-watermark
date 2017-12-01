#!/usr/local/bin/python3

from image import Image
import struct
import math
from misc import *
import time

class BMPImage(Image):
    """BMPImage Class"""
    def __init__(self, filename):
        super(BMPImage, self).__init__(filename)

        # Opening file
        with open(filename, 'rb') as f:
            data = bytearray(f.read())

        self.filename = filename

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

        # Additional fields
        self.row_size = math.floor(float(self.bpp * self.width + 31) / 32) * 4 # size of row in bytes
        self.padding = self.row_size % int(self.bpp / 8 * self.width) # size of row padding in bytes

        # Image array
        # start_time = time.time()
        self.img_data = [[[0 for i in range(3)] for j in range(self.height)] for k in range(self.width)]
        # print(time.time() - start_time)


        # start_time = time.time()
        pointer = self.offset
        # arr = []
        for i in range(self.width):
            # arr.append([])
            for j in range(self.height):
                # arr[i].append([])
                for k in range(3):
                    # arr[i][j].append([k])
                    # arr[i][j][k] = struct.unpack_from('B', data, pointer + k)[0]
                    self.img_data[i][j][k] = struct.unpack_from('B', data, pointer + k)[0]
                    # print(i, j, k)
                pointer += 3
            pointer += self.padding
        # print(time.time() - start_time)
        # self.img_data = arr

    def getImageArray(self):
        # Refactors self.array field for algorithm module
        return self.img_data

    def setImageArray(self, img_data):
        # Refactors back img_data to normal (original) state
        self.img_data = img_data
        pass

    def write(self):
        # Writes all fields to file
        new_filename = genNewName(self.filename)
        new_data = bytearray(self.size)
        struct.pack_into("BB", new_data, 0, self.type.encode()[0], self.type.encode()[1])
        struct.pack_into("IHHIIiiHHIIiiII", new_data, 2, self.size, self.res1, self.res2, self.offset, self.dib_header_size, self.width, self.height, self.color_planes, self.bpp, self.compression, self.bm_size, self.hor_res, self.ver_res, self.num_of_colors, self.imp_colors)

        pointer = self.offset
        for i in range(self.width):
            for j in range(self.height):
                for k in range(3):
                    struct.pack_into('B', new_data, pointer + k, self.img_data[i][j][k])
                pointer += 3
            for g in range(self.padding):
                struct.pack_into('B', new_data, pointer, 0)
            pointer += self.padding

        # Opening file for writing
        with open(new_filename, 'wb') as f:
            f.write(new_data)
