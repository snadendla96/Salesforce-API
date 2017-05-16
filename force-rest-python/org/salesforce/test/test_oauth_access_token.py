from org.salesforce.util import util


if __name__ == "__main__":
    access_token = util.get_access_token()['access_token']
    print("access_token: " + access_token)