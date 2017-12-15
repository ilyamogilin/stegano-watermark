#!/usr/local/bin/python3


def genNewName(filename):
    path = filename.split('/')
    new_filename = 'new_' + path[len(path) - 1]
    del path[len(path) - 1]
    new_filename = "/".join(path) + "/" + new_filename
    return new_filename


def getExtension(filename):
    ext = filename.split('.')
    return ext[len(ext) - 1].lower()


def format_data(string):
    return bin(int.from_bytes(string.encode(), 'big'))


def reformat_data(string):
    n = int(string, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

def get_diag_index(sum):
    if (sum <= 7):
        return 0
    elif (sum == 14):
        return 7
    else:
        return sum % 7

def get_diag_sum(sum):
    if (sum <= 7):
        return sum
    else:
        return 7
