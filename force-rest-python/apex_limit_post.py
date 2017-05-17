#!/usr/bin/python
from org.salesforce.account.apexobject import Students

import yaml
import json


if __name__ == '__main__':
    apexobject = Students()
    f = open('test.txt', 'r').read()
    new_object = f
    apexobject.create(new_object)
    








