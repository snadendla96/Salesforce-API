import pprint
import json

from org.salesforce.util import util


class Students:
    url = util.apex_rest + 'Students'
    new_object = {}

    def __init__(self):
        self.access_token = util.get_access_token()['access_token']
        self.headers = {'Authorization': 'Bearer ' + self.access_token}

    def create(self, new_object_p):
        #print new_object_p,'objectp'
        self.new_object = new_object_p
        access_token = util.get_access_token()['access_token']
        data = util.apexrest_post('Students', self.new_object)
        print data
        #pretty printer is not good in showing the output
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(json.loads(data))
      

    def delete(self, obj_id):
        util.apexrest_delete('Students', obj_id)
      

    def get_list(self):
        return util.get_sobject_list('Students')
        
        
    def update(self, new_object_p):
        self.new_object = new_object_p
        access_token = util.get_access_token()['access_token']
        data = util.apexrest_patch('Students', self.new_object)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(json.loads(data))
        print(data)