from org.salesforce.wave.insights_external_data import InsightsExternalData


if __name__ == "__main__":
    insights_external_data = InsightsExternalData()
    data_id = "06V280000008tLMEAY"
    data = {
        "Action": "Process"
    }
    response = insights_external_data.patch(data_id, data)
    print(response)







