import pprint
import json

from org.salesforce.wave.resources import Resource


if __name__ == "__main__":
    resource = Resource()
    data = resource.get_list()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.loads(data))
    print(data)
