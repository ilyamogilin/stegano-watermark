#!/usr/local/bin/python3

class Image(object):
    """Abstract Image Class"""
    def __init__(self, name, key, message):
        super(Image, self).__init__()
        self.name = name
        self.key = key
        self.message = message

    def encrypt(img_data, message):
        # Encrypts image with message
        pass

    def decrypt(img_data, key):
        # Decrypts image with key
        pass

    def getImageArray():
        # Refactors self.array field for algorithm module
        pass

    def setImageArray(img_data):
        # Refactors back img_data to normal (original) state
        pass

    def write():
        # Writes all fields to file
        pass
