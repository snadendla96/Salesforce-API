import pprint
import json

from org.salesforce.account.account import Account


if __name__ == "__main__":
    account = Account()
    data = account.get_list()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.loads(data))
    print(data)
