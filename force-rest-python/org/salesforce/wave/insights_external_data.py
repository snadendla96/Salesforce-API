import pprint
import json

from org.salesforce.util import util


class InsightsExternalData:
    url = util.base_url + '/'

    def __init__(self):
        self.access_token = util.get_access_token()['access_token']
        self.headers = {'Authorization': 'Bearer ' + self.access_token}

    def upload_metadata(self, metadata):
         data = util.create_sobject('InsightsExternalData', metadata)
         print(data)
         return data

    def upload_part(self,  data):
         access_token = util.get_access_token()['access_token']
         response = util.create_sobject('InsightsExternalDataPart', data)
         return response

    def delete_external_data(self, id):
         util.delete_sobject('InsightsExternalData', id)

    def delete_external_data_part(self, id):
         util.delete_sobject('InsightsExternalDataPart', id)

    def patch(self, id,  data):
         #access_token = util.get_access_token()['access_token']
         response = util.patch_sobject('InsightsExternalData', id, data)
         return response

    def describe(self):
        return util.get_sobject_list('InsightsExternalData/')

    def get_detail(self, id):
        return util.get_sobject_list('InsightsExternalData/' + id)

