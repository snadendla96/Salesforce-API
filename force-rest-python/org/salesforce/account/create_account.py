from org.salesforce.account.account import Account


if __name__ == "__main__":
    account = Account()
    new_account = {"Name": "BlueDart__2"}
    
    print new_account
    account.create(new_account)




