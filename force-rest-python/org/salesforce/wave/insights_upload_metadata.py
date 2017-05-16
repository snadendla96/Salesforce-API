from org.salesforce.wave.insights_external_data import InsightsExternalData
from org.salesforce.wave.wave_util import read_file
from org.salesforce.wave.wave_util import encode
import json

def upload_metadata(_path, edge_mart_alias, _format, _operation, _action):
    insights_external_data = InsightsExternalData()
    input_str = read_file(_path)
    encoded_metadata = encode(input_str)
    metadata = {}
    metadata["Format"] = _format
    metadata["Operation"] = _operation
    metadata["Action"] = _action
    metadata["EdgemartAlias"] = edge_mart_alias
    metadata["MetadataJson"] = encoded_metadata.decode('utf-8')
    response_local = insights_external_data.upload_metadata(metadata)
    json_data = json.loads(str(response_local))
    return json_data['id']

if __name__ == "__main__":

    path = '/home/ubuntu/work/force-rest-python/data/test_metadata_v1.json'
    format = 'csv'
    operation = 'Overwrite'
    action = 'None'
    edge_mart_alias = 'OppExtData1'
    response = upload_metadata(path, edge_mart_alias, format, operation, action)
    print(response)




