#!/usr/local/bin/python3
import base64

class Image(object):
    """Abstract Image Class"""
    def __init__(self, name, key, message):
        super(Image, self).__init__()
        self.name = name
        self.key = key
        self.message = message

    def encrypt(self, img_data, message):
        if len(img_data) == 0 or len(message) == 0:
            return

        if len(message) > len(img_data) ** 2:
            print('the file too short for your message')
            return

        l = 0.1
        array_counter = 0
        key = ''
        message_counter = 0

        for x in img_data:
            for y in x:

                if message_counter == len(message) - 1:
                    break

                if y[0] == 255 and message[message_counter] == '1':
                    array_counter += 1
                    continue

                if y[0] == 0 and message[message_counter] == '0':
                    array_counter += 1
                    continue

                bright = 0.3 * y[2] + 0.59 * y[1] + 0.11 * y[0]
                new_blue = y[0] + l * bright if int(message[message_counter]) == 1 else y[0] - l * bright
                new_blue = int(new_blue)

                if new_blue <= 0:
                    array_counter += 1
                    continue

                y[0] = new_blue

                array_counter += 1
                message_counter += 1

                key += str(img_data.index(x)) + ' ' + str(x.index(y)) + ' | '

        if message_counter < len(message) - 1:
            print('the file too short for your message')
            return

        self.key = base64.b64encode(bytes(key))
        return img_data

    def decrypt(self, img_data, key):
        # Decrypts image with key
        pass

    def getImageArray(self):
        # Refactors self.array field for algorithm module
        pass

    def setImageArray(self, img_data):
        # Refactors back img_data to normal (original) state
        pass

    def write(self):
        # Writes all fields to file
        pass
