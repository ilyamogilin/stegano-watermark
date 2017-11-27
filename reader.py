#!/usr/local/bin/python3

import struct
import math

with open('image.bmp', 'rb') as f:
    data = bytearray(f.read())

img_info = {}
img_info['type'] = data[0:2].decode() # Type
img_info['size'] = struct.unpack_from('I', data, 2)[0] # the size of the BMP file in bytes
img_info['res1'] = struct.unpack_from('H', data, 6)[0] # reserved; actual value depends on the application that creates the image
img_info['res2'] = struct.unpack_from('H', data, 8)[0] # reserved; actual value depends on the application that creates the image
img_info['offset'] = struct.unpack_from('I', data, 10)[0] # the offset, i.e. starting address, of the byte where the bitmap image data (pixel array) can be found.

# Support only for BITMAPINFOHEADER and BI_RGB compression method (no compression)
# TODO: add support for BI_BITFIELDS
img_info['dib_header_size'] = struct.unpack_from('I', data, 14)[0] # The size of DIB header
img_info['width'] = struct.unpack_from('i', data, 18)[0] # the bitmap width in pixels (signed integer)
img_info['height'] = struct.unpack_from('i', data, 22)[0] # the bitmap height in pixels (signed integer)
img_info['color_planes'] = struct.unpack_from('H', data, 26)[0] # the number of color planes (must be 1)
img_info['bpp'] = struct.unpack_from('H', data, 28)[0] # the number of bits per pixel, which is the color depth of the image. Typical values are 1, 4, 8, 16, 24 and 32.
img_info['compression'] = struct.unpack_from('I', data, 30)[0] # the compression method being used. See the next table for a list of possible values
img_info['bm_size'] = struct.unpack_from('I', data, 34)[0] # the image size. This is the size of the raw bitmap data; a dummy 0 can be given for BI_RGB bitmaps.
img_info['hor_res'] = struct.unpack_from('i', data, 38)[0] # the horizontal resolution of the image. (pixel per metre, signed integer)
img_info['ver_res'] = struct.unpack_from('i', data, 42)[0] # the vertical resolution of the image. (pixel per metre, signed integer)
img_info['num_of_colors'] = struct.unpack_from('I', data, 46)[0] # the number of colors in the color palette, or 0 to default to 2^n
img_info['imp_colors'] = struct.unpack_from('I', data, 50)[0] # the number of important colors used, or 0 when every color is important; generally ignored

# print image info
for i in img_info.keys():
    print(i, ':', img_info[i])

bpp = img_info['bpp']
width = img_info['width']
height = img_info['height']
offset = img_info['offset']
row_size = math.floor(float(bpp * width + 31) / 32) * 4 # TODO: move to class' field?
padding = row_size % int(bpp / 8 * width) # TODO: move to class' field?

img_data = [[[0 for i in range(3)] for j in range(height)] for k in range(width)]

pointer = offset
for i in range(height):
    for j in range(width):
        for k in range(3):
            img_data[i][j] = [struct.unpack_from('B', data, pointer)[0], struct.unpack_from('B', data, pointer + 1)[0], struct.unpack_from('B', data, pointer + 2)[0]]
        pointer += 3
    pointer += padding
print(img_data)
