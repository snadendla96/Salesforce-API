import pprint
import json

from org.salesforce.util import util


class Resource:
    url = util.base_url + '/'
    new_account = {}

    def __init__(self):
        self.access_token = util.get_access_token()['access_token']
        self.headers = {'Authorization': 'Bearer ' + self.access_token}

    # def create(self, new_account_p):
    #     self.new_account = new_account_p
    #     access_token = util.get_access_token()['access_token']
    #     data = util.create_sobject('Account', self.new_account)
    #     pp = pprint.PrettyPrinter(indent=4)
    #     pp.pprint(json.loads(data))
    #     print(data)
    #
    # def delete(self, account_id):
    #     util.delete_sobject('Account', account_id)

    def get_list(self):
        return util.get_sobject_list_wave(util.wave_base_url, '')