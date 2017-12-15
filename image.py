#!/usr/local/bin/python3
import base64
from misc import format_data, reformat_data
import time

class Image(object):
    """Abstract Image Class"""
    def __init__(self, name):
        super(Image, self).__init__()
        self.name = name

    def encrypt(self, message):

        message = format_data(message).replace('0b', '')

        img_data = self.getImageArray()

        if len(img_data) == 0 or len(message) == 0:
            return

        if len(message) > len(img_data) ** 2:
            print('the file too short for your message')
            return

        l = 0.1
        delta = 2
        array_counter = 0
        key = ''
        message_counter = 0

        for x in range(delta, len(img_data)):
            for y in range(delta, x + 1, delta):
                if message_counter == len(message):
                    break

                if img_data[x][y][0] == 255 and message[message_counter] == '1':
                    array_counter += 1
                    continue

                if img_data[x][y][0] == 0 and message[message_counter] == '0':
                    array_counter += 1
                    continue

                bright = 0.3 * img_data[x][y][2] + 0.59 * img_data[x][y][1] + 0.11 * img_data[x][y][0]
                new_blue = img_data[x][y][0] + l * bright if int(message[message_counter]) == 1 else img_data[x][y][0] - l * bright
                new_blue = int(new_blue)

                if new_blue <= 0:
                    array_counter += 1
                    continue

                img_data[x][y][0] = new_blue

                array_counter += 1 + delta
                message_counter += 1

                key += str(x) + ' ' + str(y) + ' | '

        if message_counter < len(message) - 1:
            print('the file too short for your message')
            return

        key = base64.b64encode(bytes(key, 'utf-8'))
        self.setImageArray(img_data)
        return key

    def decrypt(self, key):
        img_data = self.getImageArray()
        key = base64.b64decode(bytes(key, 'utf-8')).decode()

        key_arr = key.split('|')
        del key_arr[len(key_arr) - 1]
        m = ''
        for point in key_arr:
            point_arr = point.strip().split(' ')

            x = int(point_arr[0])
            y = int(point_arr[1])

            b_b = img_data[x][y + 1][0] + img_data[x][y - 1][0] + img_data[x - 1][y][0] + img_data[x + 1][y][0]
            b_b += img_data[x][y + 2][0] + img_data[x][y - 2][0] + img_data[x - 2][y][0] + img_data[x + 2][y][0]
            b_b /= 8

            if (img_data[x][y][0] > b_b):
                m += '1'
            else:
                m += '0'
        m = reformat_data('0b' + m)

        return m

    def getImageArray(self):
        # Refactors self.array field for algorithm module
        pass

    def setImageArray(self, img_data):
        # Refactors back img_data to normal (original) state
        pass

    def write(self):
        # Writes all fields to file
        pass
