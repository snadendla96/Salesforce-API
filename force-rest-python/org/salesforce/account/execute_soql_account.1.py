from org.salesforce.util import util
import pprint
import json

if __name__ == "__main__":
    soql = """SELECT+name+from+Account"""
    data = util.execute_soql(soql)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.loads(data))
    #print(data)





