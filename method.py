def kdb_method(arr=[], msg=[]):

    if len(arr) == 0 or len(msg) == 0:
        return

    l = 0.1
    i = 0
    for index in arr:
        if i == len(msg):
            break

        Y = 0.3 * index[0] + 0.59 * index[1] + 0.11 * index[2]
        print(str(index[2]) + "  changed to")

        index[2] += l * Y if msg[i] == 1 else - l * Y
        index[2] = int(index[2])
        i += 1
        print (str(index[2]) + '\n')
    return arr
