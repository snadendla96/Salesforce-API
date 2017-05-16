from org.salesforce.util import util
import pprint
import json

if __name__ == "__main__":
    soql = """SELECT+name+from+Student__c"""
    data = util.execute_soql(soql)
    #print data
    pp = pprint.PrettyPrinter(indent=4)
    #print pp
    pp.pprint(json.loads(data))
    #print pp
    #print(data)




