#!/usr/bin/python
# -*- coding: utf-8 -*-
from org.salesforce.account.apexobject import Students

import yaml
import json

# new_object =  rs
# apexobject.create(new_object)

if __name__ == '__main__':
    apexobject = Students()
    f = open('test.txt', 'r').read()
    new_object = f
    #print new_object
    apexobject.create(new_object)









# if __name__ == "__main__":
#     apexobject = Students()
#     fs= {
#      "wrpVals": {
# "ConcurrentAsyncGetReportInstances": "ConcurrentAsyncGetReportInstances",
#       "Max": "200",
#       "Remaining": "200",
#      "ConcurrentSyncReportRuns":"ConcurrentSyncReportRuns",
#       "Max1": "20",
#       "Remaining1": "20",
# ....  "DailApiRequest":"DailApiRequest",
# ....  "DAPiMax":"1500",
# ....  "DAPIRemaining":"14976",
#       "Ant":"Ant Migration Tool",
#       "AntMax":"0",
#       "AntRemaining":"0",
#       "App":"Chemical",
#       "AppMax":"0",
#       "AppRemaining":"0",
#       "DataloaderBulk":"Dataloader Bulk",
#       "DMax":"0",
#       "DRemaining":"0",
#       "DPartner":"Dataloader Partner",
# ....    "DPMax":"0",
# ........"DpRemaining":"0",
# ........"FIde":"Force.com IDE",
#   "Fmax":"0",
# ........"FRemaining":"0",
# ........"SFMD":"Mobile Dashboards",
# ........"SFMDMax":"0",
# ........"SFMDRemaining":"0",
# ........"SFTouch":"Salesforce Touch",
# ........"SFTMax":"0",
# ........"SFTRemaining":"0",
# ........"SFOutlook":"Outlook",
# ........"SFOMax":"0",
# ........"SFORemaining":"0"

#     }
# ........}
# new_object =  fs
# apexobject.create(new_object)


			