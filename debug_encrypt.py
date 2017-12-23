from misc import format_data, reformat_data


def encrypt_nw(img_data, message):
    # message += 'EoM'  # end of message trigger
    print (img_data, message)
    message = format_data(message).replace('0b', '')
    # img_data = self.getImageArray()
    if len(img_data) == 0 or len(message) == 0:
        print('len(img_data) == 0 or len(message) == 0, line:97')
        return

    if len(message) > len(img_data) ** 2 / 5:
        print('the file too short for your message')
        return

    l = 0.1
    delta = 2
    array_counter = 0
    key = ''
    message_counter = 0
    # print(len(img_data))

    for x in range(delta, len(img_data) - 3):
        for y in range(delta, x - delta, delta):
            print(x, y)
            if y >= len(img_data[x]) - delta:
                print('y >= len(img_data[x]) - delta, line:115')

                break
            #
            # if message_counter == len(message) - 1:
            #     message_counter = 0

            if img_data[x][y][0] == 255 and message[message_counter] == '1':
                array_counter += 1
                continue

            if img_data[x][y][0] == 0 and message[message_counter] == '0':
                array_counter += 1
                continue

            bright = 0.3 * img_data[x][y][2] + 0.59 * img_data[x][y][1] + 0.11 * img_data[x][y][0]
            new_blue = img_data[x][y][0] + l * bright if int(message[message_counter]) == 1 else img_data[x][y][
                                                                                                     0] - l * bright
            new_blue = int(new_blue)

            if new_blue <= 0 or new_blue >= 255:
                array_counter += 1
                continue

            img_data[x][y][0] = new_blue

            array_counter += 1 + delta
            message_counter += 1

            key += str(x) + ' ' + str(y) + ' | '

    # key = base64.b64encode(bytes(key, 'utf-8'))
    # self.setImageArray(img_data)
    return key

