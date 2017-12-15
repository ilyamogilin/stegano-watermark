#!/usr/local/bin/python3

from factory import ImageFactory
import time
from misc import genNewName
import matplotlib.pyplot as plot
import multiprocessing

# images = ['images/16.bmp']

images = ['images/Tulips.bmp',
          'images/baboon.bmp',
          'images/bmp-sample.bmp',
          'images/sample.bmp',
          'images/5.bmp',
          'images/7.bmp',
          'images/13.bmp',
          'images/10.bmp',
          'images/3.bmp',
          'images/16.bmp',
          'images/11.bmp',
          'images/12.bmp']
image_sizes = [580, 710, 1110, 1420, 3730, 4470, 6430, 6590, 6598, 7030, 8730, 9000]
messages = ['HelloWorld', 'qwertyuiopasdfghjklz', 'qwertyuiopasdfghjklz qwertyuiopasdfghjklz eeeBoii']

factory = ImageFactory()


def test_parser(path):
    encrypt_times = []
    parse_times = []
    write_times = []
    decrypt_times = []
    for i in range(0, 3):
        start_time = time.time()
        img = factory.createImage(path)
        parse_times.append(time.time() - start_time)

        # start_time_e = time.time()
        # key = img.encrypt("jyfukdwldnasdqwd")
        # encrypt_times.append(time.time() - start_time_e)

        # start_time_write = time.time()
        # img.write()
        # write_times.append(time.time() - start_time_write)

        #new_img = factory.createImage(genNewName(path))

        # start_time_d = time.time()
        # message = new_img.decrypt(key)
        # decrypt_times.append(time.time() - start_time_d)

    return {'parse_times': parse_times,
            'encrypt_times': encrypt_times,
            'decrypt_times': decrypt_times,
            'write_times': write_times}


def image_iterator(image):
    tests = test_parser(image)
    all_parse_time = 0

    for t in tests['parse_times']:
        all_parse_time += t

    obj = {'image': image,
           'parse_times': tests['parse_times'],
           'parse_time':  all_parse_time / len(tests['parse_times']),
           'encrypt_times': tests['encrypt_times'],
           'decrypt_times': tests['decrypt_times'],
           'write_times': tests['write_times']}

    return obj


def plots(x, y):
    print(x, y)
    plot.plot(x, y, 'go')
    plot.title('parsing time = f (image size)')
    plot.legend()
    plot.xlabel('image size (Kb)')
    plot.ylabel('time (s)')
    plot.savefig('test/parse_time/parsing_time.png')


if __name__ == "__main__":
    with multiprocessing.Pool(4) as p:
        start_time = time.time()

        obj = p.map(image_iterator, images)
        x_x = []
        for o in obj:
            x_x.append(o['parse_time'])

        plots(image_sizes, x_x)

        print((time.time() - start_time) / 60)
