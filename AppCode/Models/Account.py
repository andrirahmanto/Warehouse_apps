import pymongo

class Account():

    def __init__(self,username = None):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["mongowarehouse"]
        self.col_account = db["account"]
        if  username:
            self.username = username

    # Getter
    def getusername(self):
        return self.username

    def getname(self):
        get = self.col_account.find_one({'username':self.username})
        if get == None:
            return None
        return get['name']

    def getpassword(self):
        get = self.col_account.find_one({'username':self.username})
        if get == None:
            return None
        return get['password']

    def getrole(self):
        get = self.col_account.find_one({'username':self.username})
        if get == None:
            return None
        return get['role']

    # Setter
    def setname(self,newname):
        query = {"username": self.username}
        set = {"$set":{"name":newname}}
        return self.col_account.update_one(query,set)

    def setpassword(self, newpassword):
        query = {"username": self.username}
        set = {"$set": {"password": newpassword}}
        return self.col_account.update_one(query, set)

    def setrole(self,newrole):
        query = {"username": self.username}
        set = {"$set":{"role":newrole}}
        return self.col_account.update_one(query,set)

    # Add & Delete
    def addaccount(self,username,password,name,role):
        dict_account = {"username":username,"password":password,"name":name,"role":role}
        return self.col_account.insert_one(dict_account)

    def delaccount(self,username):
        query = {"username":username}
        return self.col_account.delete_one(query)

    # Method
    def getdataaccount(self):
        return self.col_account.find_one({'username':self.username})

    def getlistusernamename(self):
        listusernamename = []
        for accountname in self.col_account.find():
            listusernamename.append(accountname["username"])
        return listusernamename

    def gettabeldata(self):
        listdata = []
        for data in self.col_account.find({}, {"_id": 0}):
            listdata.append(data)
        return listdata
