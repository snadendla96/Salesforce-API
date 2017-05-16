from org.salesforce.account.apexobject import Students

if __name__ == "__main__":
    apexobject = Students()
    obj_id = 'a0346000002AAef'
    apexobject.delete(obj_id)
