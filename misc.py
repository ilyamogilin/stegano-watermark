#!/usr/local/bin/python3

def gen_new_name(filename):
    path = filename.split('/')
    new_filename = 'new_' + path[len(path) - 1]
    del path[len(path) - 1]
    new_filename = "/".join(path) + "/" + new_filename
    return new_filename
