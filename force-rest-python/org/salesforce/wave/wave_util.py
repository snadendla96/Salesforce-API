__author__ = 'rajdeep dua'

import base64


def encode(data):
    return base64.b64encode(bytes(data,'utf-8'))


def read_file(path):
    local_file = open(path, 'r')
    file_content = local_file.read()
    return file_content
