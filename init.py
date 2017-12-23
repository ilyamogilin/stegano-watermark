#!/usr/local/bin/python3

from factory import ImageFactory

print('Stegano-watermark v1.0: Kutter-Jordan-Bossen method')
print('Specify the action: encrypt (e) or decrypt (d)')
action = input()

if (action == 'e'):

    print('Enter the path to image:')
    path = input()
    print('Enter the message to encrypt:')
    message = input()
    print('Enter the path to key file (image.key):')
    key_filename = input()

    if key_filename == '':
        key_filename = 'image.key'

    factory = ImageFactory()
    img = factory.createImage(path)
    key = img.encrypt(message).decode('utf-8')
    img.write()

    with open(key_filename, 'w') as f:
        f.write(key)

    print('Image successfully encrypted with key stored in', key_filename)
    # print('Image successfully encrypted with key:', key.decode('utf-8'))
    # print('Image successfully encrypted with key:', key)

elif (action == 'd'):

    print('Enter the path to image:')
    path = input()
    print('Enter the path to key file (image.key):')
    key_filename = input()

    if key_filename == '':
        key_filename = 'image.key'

    with open(key_filename, 'r') as f:
        key = f.read()

    factory = ImageFactory()
    img = factory.createImage(path)
    message = img.decrypt(key)
    print('Encrypted message:', message)

else:
    print('Invalid action')
    exit(-1)
# ---------------------------------------

# factory = ImageFactory()
# img = factory.createImage('images/google.jpg')
