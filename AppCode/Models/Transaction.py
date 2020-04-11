import pymongo
from bson.objectid import ObjectId

class Transaction():

    def __init__(self, iditem = None):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["mongowarehouse"]
        self.col_transaction = db["transaction"]
        if iditem:
            self.idtransaction = ObjectId(iditem)

    # Getter
    def getcashiername(self):
        return self.col_transaction.find_one({"_id": self.idtransaction})["cashiername"]

    def getitemname(self):
        return self.col_transaction.find_one({"_id":self.idtransaction})["itemname"]

    def getamountitem(self):
        return self.col_transaction.find_one({"_id": self.idtransaction})["amountitem"]

    def getprice(self):
        return self.col_transaction.find_one({"_id":self.idtransaction})["price"]

    def gettotalprice(self):
        return self.col_transaction.find_one({"_id": self.idtransaction})["totalprice"]

    # Setter
    def setcahseirname(self, newcashiername):
        query = {"_id": self.idtransaction}
        set = {"$set": {"itemname": newcashiername}}
        return self.col_transaction.update_one(query, set)

    def setitemname(self, newitemname):
        query = {"_id": self.idtransaction}
        set = {"$set": {"itemname": newitemname}}
        return self.col_transaction.update_one(query, set)

    def setamountitem(self, newamountitem):
        query = {"_id": self.idtransaction}
        set = {"$set": {"amountitem": newamountitem}}
        return self.col_transaction.update_one(query, set)

    def setprice(self, newprice):
        query = {"_id": self.idtransaction}
        set = {"$set": {"price": newprice}}
        return self.col_transaction.update_one(query, set)

    def settotalprice(self,newtotalprice):
        query = {"_id": self.idtransaction}
        set = {"$set": {"price": newtotalprice}}
        return self.col_transaction.update_one(query, set)

    # Add
    def addtransaction(self, cashiername, itemname, amountitem, price, totalprice):
        query = {"cashiername":cashiername,"itemname":itemname,"amountitem":amountitem,"price":price,"totalprice":totalprice}
        return self.col_transaction.insert_one(query)

    #method
    def getdatatransaction(self):
        # Return json/dict
        return self.col_transaction.find_one({"_id": self.idtransaction},{"_id":0})

    def getallidtransaction(self):
        # Return List
        list = []
        alldata = self.col_transaction.find({})
        for data in alldata:
            id = ObjectId(data["_id"])
            list.append(id)
        return list

    def getalldatatransaction(self):
        # Return list
        listid = self.getallidtransaction()
        listalldatatransaction = []
        for id in listid:
            id = Transaction(id)
            listalldatatransaction.append(id.getdatatransaction())
        return listalldatatransaction

    def gettabeldata(self):
        # Return dict in list
        listdata = []
        for data in self.col_transaction.find({}, {"_id": 0}):
            listdata.append(data)
        return listdata

