from org.salesforce.util import util
import pprint
import json

if __name__ == "__main__":
    soql = """SELECT+Id+from+insightsexternaldatapart"""
    data = util.execute_soql(soql)
    #print(data)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.loads(data))
    print(data)





