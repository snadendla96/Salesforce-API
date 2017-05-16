from org.salesforce.wave.insights_external_data import InsightsExternalData

if __name__ == "__main__":

    insights_external_data = InsightsExternalData()
    id = '06W280000008snzEAA'
    response  = insights_external_data.delete_external_data_part(id)
    print(response)

