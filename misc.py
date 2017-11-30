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
