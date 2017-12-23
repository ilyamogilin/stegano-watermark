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

        if len(message) > len(img_data) ** 2 / 5:
            print('the file too short for your message')
            return

        l = 0.1
        delta = 2
        array_counter = 0
        key = ''
        message_counter = 0

        for x in range(delta, len(img_data) - 1, delta + 1):
            if message_counter == len(message):
                break
            for y in range(delta, len(img_data[x]), delta + 1):
                #
                if message_counter == len(message):
                    break

                if y >= len(img_data[x]) - delta:
                    break

                if img_data[x][y][0] >= 240 and message[message_counter] == '1':
                    array_counter += 1
                    continue

                if img_data[x][y][0] <= 15 and message[message_counter] == '0':
                    array_counter += 1
                    continue

                average_value = (img_data[x][y + 1][1] + img_data[x][y - 1][1] + img_data[x - 1][y][1] + img_data[x + 1][y][1] +
                       img_data[x][y + 2][1] + img_data[x][y - 2][1] + img_data[x - 2][y][1] + img_data[x + 2][y][
                           1]) / (4 * delta)

                bright = 0.3 * img_data[x][y][0] + 0.59 * img_data[x][y][1] + 0.11 * img_data[x][y][1]
                new_blue = average_value + l * bright if int(message[message_counter]) == 1 else average_value - l * bright
                new_blue = int(new_blue)

                if new_blue <= 0 or new_blue >= 255:
                    array_counter += 1
                    continue

                img_data[x][y][1] = new_blue

                array_counter += 1 + delta
                message_counter += 1

                key += str(x) + ' ' + str(y) + ' | '

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

            b_b = (img_data[x][y + 1][1] + img_data[x][y - 1][1] + img_data[x - 1][y][1] + img_data[x + 1][y][1] + img_data[x][y + 2][1] + img_data[x][y - 2][1] + img_data[x - 2][y][1] + img_data[x + 2][y][1]) / (4 * 2)

            if (img_data[x][y][1] > b_b):
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
