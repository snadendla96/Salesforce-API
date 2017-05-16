from org.salesforce.account.account import Account

if __name__ == "__main__":
    account = Account()
    account_id = '0012800000mkMrpAAE'
    account.delete(account_id)

