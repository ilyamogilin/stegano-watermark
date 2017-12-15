#!/usr/local/bin/python3

from image import Image
import struct
import math
from misc import *
from HuffmanTree import *

class JPEGImage(Image):
    """JPEGImage Class"""
    def __init__(self, filename):
        super(JPEGImage, self).__init__(filename)

        # 1. Opening file
        with open(filename, 'rb') as f:
            data = bytearray(f.read())

        self.filename = filename

        # 2. Parsing quantisation tables
        quant_tables = []
        marker_pos = 0

        while (data.find(b'\xff\xdb', marker_pos) != -1):

            marker_pos = data.find(b'\xff\xdb', marker_pos)
            quan_header_size = struct.unpack_from('>H', data, marker_pos + 2)[0] # Size of quantisation table
            together_byte = data[marker_pos + 4]
            val_size = int(together_byte / 16) # The byte length of each element in table
            table_id = together_byte % 16 # Quantasation table identifier
            quant_table = [[0 for i in range(8)] for j in range(8)]

            # TODO: Replace 'B' in cycle with function depending on val_size
            for sum in range(15):
                # print('sum =', sum)
                # print('diag_sum =', get_diag_sum(sum))
                if (sum % 2 == 0):
                    for i in range(get_diag_index(sum), get_diag_sum(sum) + 1)[::-1]:
                        # print(i, sum - i)
                        quant_table[i][sum - i] = struct.unpack_from('B', data, marker_pos + 5 + (i * 8) + (sum - i))[0]
                else:
                    for i in range(get_diag_index(sum), get_diag_sum(sum) + 1):
                        # print(i, sum - i)
                        quant_table[i][sum - i] = struct.unpack_from('B', data, marker_pos + 5 + (i * 8) + (sum - i))[0]

            marker_pos += 1
            # quant_tables.append([table_id, quant_table])
            quant_tables.append(quant_table)

        # quant_tables = sorted(quant_tables, key=lambda x: x[0])

        # 3. Parsing encoding type: Baseline DCT or Progressive DCT
        # Supprot only for Baseline DCT
        marker_pos = data.index(b'\xff\xc0')
        encoding_header_size = struct.unpack_from('>H', data, marker_pos + 2)[0] # size of section
        comp_size = struct.unpack_from('B', data, marker_pos + 4)[0] # size of section # bits per one component of pixel
        height = struct.unpack_from('>H', data, marker_pos + 5)[0] # height of image in bytes(?)
        width = struct.unpack_from('>H', data, marker_pos + 7)[0] # width of image in bytes(?)
        component_quantity = struct.unpack_from('B', data, marker_pos + 9)[0] # number of components in pixel

        print('\nComponent parameters:')
        print('-------------------------------')
        pos = marker_pos + 10
        comp_params = [] # comp_params[i] = [component_id, hor_density, ver_density, quant_table_id]
        for i in range(component_quantity):
            comp_params.append([struct.unpack_from('B', data, pos)[0], int(data[pos + 1] / 16), data[pos + 1] % 16, struct.unpack_from('B', data, pos + 2)[0]])
            print(comp_params[i])
            pos += 3

        # 4. Parsing Huffman tables
        huff_tables = []
        marker_pos = 0
        class_counter = 0
        val_array = [0 for i in range(2)]

        while (data.find(b'\xff\xc4', marker_pos) != -1):
            huff_quantity = [] # huffman_length[i] - quantity of codes of i length
            huff_codes = [] # huffman_codes[i] - code value
            marker_pos = data.find(b'\xff\xc4', marker_pos)
            start_pos = marker_pos
            huff_size = struct.unpack_from('>H', data, marker_pos + 2)[0] # size of Huffman table
            together_byte = data[marker_pos + 4]
            huff_table_class = int(together_byte / 16) # class of table: AC (1) or DC (0) coefficients
            huff_table_id = together_byte % 16 # Huffman table identifier

            marker_pos += 5

            for i in range(16):
                # print(i, struct.unpack_from('B', data, marker_pos + i)[0])
                huff_quantity.append(struct.unpack_from('B', data, marker_pos + i)[0])

            marker_pos += 16
            # print(marker_pos, start_pos + huff_size + 2)

            for i in range(marker_pos, start_pos + huff_size + 2):
                huff_codes.append(struct.unpack_from('B', data, i)[0])

            # huff_tables.append([huff_table_id, huff_table_class, huff_quantity, huff_codes])
            # huff_tables.append({"id" : huff_table_id, "class" : huff_table_class, "quantity" : huff_quantity, "codes" : huff_codes})
            val_array[class_counter] = {"quantity" : huff_quantity, "codes" : huff_codes}
            if (class_counter == 1):
                huff_tables.append(val_array)
                val_array = [0 for i in range(2)]
            class_counter = (class_counter + 1) % 2


        # huff_tables = sorted(huff_tables, key=lambda x: x[0])

        nodes = []
        print('\nHuffman tables and building trees:')
        print('-------------------------------')
        for i in range(len(huff_tables)):
            nodes.append([])
            for j in range(2):
                nodes[i].append(HuffmanNode())
                create_tree(nodes[i][j], huff_tables[i][j]['quantity'], huff_tables[i][j]['codes'], -1, 0)
                print('id =', i)
                print('table_class =', j)
                print('huff_quantity =', huff_tables[i][j]['quantity'])
                print('huff_codes =', huff_tables[i][j]['codes'])
                print('-------------------------------')

        # # 4. Building Huffman tree
        # print('\nTrees:')
        # print('-------------------------------')
        #
        # node = HuffmanNode()
        # create_tree(node, huff_tables[0][1]['quantity'], huff_tables[0][1]['codes'], -1, 0)

        # 5. Parsing huff_table_ids for components
        print('\nComponent parameters UPD (+ AC and DC tales\' IDs):')
        print('-------------------------------')
        marker_pos = data.index(b'\xff\xda')
        marker_pos += 5

        # comp_params[i] = [component_id, hor_density, ver_density, quant_table_id, dc_id, ac_id]
        for i in range(component_quantity):
            comp_params[i].append(int(data[marker_pos + 1] / 16))
            comp_params[i].append(data[marker_pos + 1] % 16)
            print(comp_params[i])
            marker_pos += 2

        # 6. Reading image array
        marker_pos += 3
        final_pos = data.index(b'\xff\xd9')

    def getImageArray(self):
        # Refactors self.array field for algorithm module
        return self.img_data

    def setImageArray(self, img_data):
        # Refactors back img_data to normal (original) state
        self.img_data = img_data
        pass

    def write(self):
        # Writes all fields to file
        pass
