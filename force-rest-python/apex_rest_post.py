from org.salesforce.account.apexobject import Students

import yaml
import json


if __name__ == "__main__":
    apexobject = Students()
    rs={  
        "name":"nadendla"
           }
    new_object =  rs
    apexobject.create(new_object)

