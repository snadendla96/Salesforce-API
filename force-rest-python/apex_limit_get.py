#!/usr/bin/python
from org.salesforce.util import util
import pprint
import json
from collections import OrderedDict


# get

if __name__ == '__main__':
    data = util.apexlimit()
    print data
    
    # pp = pprint.PrettyPrinter(depth=2)
    # pp.pprint(json.loads(data))
    # print data
   
    # opt= json.loads(data, object_pairs_hook=OrderedDict)
    # s=json.dumps(opt, indent=2,sort_keys=True)
    # print s
   
    #########################################Working Code#####################################################
#     d = opt
# for k, v in d.items():
#          s=(k, v)
#          print s
#  #########################################Working Code#####################################################
