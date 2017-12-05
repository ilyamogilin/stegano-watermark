#!/usr/local/bin/python3

from factory import ImageFactory

print('Stegano-watermark v1.0: Kutter-Jordan-Bossen method')
print('Specify the action: encrypt (e) or decrypt (d)')
action = input()

if (action == 'e'):

    print('Enter the path to file:')
    path = input()
    print('Enter the message to encrypt:')
    message = input()

    factory = ImageFactory()
    img = factory.createImage(path)
    key = img.encrypt(message)
    img.write()
    print('Image successfully encrypted with key:', key.decode('utf-8'))

elif (action == 'd'):

    print('Enter the path to file:')
    path = input()
    print('Enter the key:')
    key = input()

    factory = ImageFactory()
    img = factory.createImage(path)
    message = img.decrypt(key)
    print('Encrypted message:', message)

else:
    print('Invalid action')
    exit(-1)
