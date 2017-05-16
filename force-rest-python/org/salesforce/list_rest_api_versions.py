import json
import pprint

from org.salesforce.util import util


conn = util.get_connection()
conn.request("GET", "/services/data/")
res = conn.getresponse()
data = res.read().decode("utf-8")

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(json.loads(data))

