#!/usr/local/bin/python3

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
        l = 0.1
        i = 0
        for x in img_data:
            for y in x:
                if i == len(message):
                    break
                Y = 0.3 * y[2] + 0.59 * y[1] + 0.11 * y[0]
                y[0] += l * Y if message[i] == 1 else - l * Y
                y[0] = int(y[0])
                if y[0] <= 0:
                    y[0] = 0
                i += 1
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
