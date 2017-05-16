from org.salesforce.wave.insights_external_data import InsightsExternalData
from org.salesforce.wave.wave_util import read_file
from org.salesforce.wave.wave_util import encode

def upload_part(path, data_id, part_number):
    insights_external_data = InsightsExternalData()
    input_str = read_file(path)
    encoded_data = encode(input_str)
    data = {}
    data['InsightsExternalDataId'] = data_id
    data['PartNumber'] = part_number
    data['DataFile'] = encoded_data.decode('utf-8')
    _response = insights_external_data.upload_part(data)
    return _response

if __name__ == "__main__":
    path = '/home/ubuntu/work/force-rest-python/data/test_file_v1.csv'
    id = '06V280000008tLMEAY'
    part_number = '1'
    response = upload_part(path, id, part_number)
    print(response)







