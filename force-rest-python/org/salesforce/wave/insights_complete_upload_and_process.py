from org.salesforce.wave.insights_upload_metadata import upload_metadata
from org.salesforce.wave.insights_upload_part import upload_part
from org.salesforce.wave.insights_external_data import InsightsExternalData


if __name__ == "__main__":
    meta_path = '/home/ubuntu/work/force-rest-python/data/test_metadata_v1.json'
    format = 'csv'
    operation = 'Overwrite'
    action = 'None'
    edge_mart_alias = 'BadgeAnalysis_v1'
    id = upload_metadata(meta_path, edge_mart_alias, format, operation, action)
    print('id:' + id)

    path = '/home/ubuntu/work/force-rest-python/data/test_file_v1.csv'
    part_number = '1'
    response = upload_part(path, id, part_number)
    print("Part Upload Response:" + response)

    insights_external_data = InsightsExternalData()
    data = {
        "Action": "Process"
    }
    response = insights_external_data.patch(id, data)
    print("Completed Processing")





