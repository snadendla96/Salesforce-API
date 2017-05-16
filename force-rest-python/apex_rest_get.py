from org.salesforce.util import util
import pprint
import json
#get
if __name__ == "__main__":
    #soql = """Account/0014600000VcqnI"""
    soql = """Students/a03460000029x92"""
    data = util.apexrest(soql)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.loads(data))
    #print(data)





