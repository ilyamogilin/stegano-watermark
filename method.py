def kdb_method(arr=[], msg=[]):

    if len(arr) == 0 or len(msg) == 0:
        return
    l = 0.1
    i = 0
    for x in arr:
        for y in x:
            if i == len(msg):
                break
            Y = 0.3 * y[2] + 0.59 * y[1] + 0.11 * y[0]
            print(str(y[0]) + "  changed to")
            y[0] += l * Y if msg[i] == 1 else - l * Y
            y[0] = int(y[0])
            if y[0] <= 0:
                y[0] = 0
            i += 1  
            print (str(y[0]) + '\n')
    return arr
