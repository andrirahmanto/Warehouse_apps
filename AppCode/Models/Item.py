import pymongo
from bson.objectid import ObjectId

class Item():

    def __init__(self, iditem = None):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["mongowarehouse"]
        self.col_item = db["item"]
        if iditem:
            self.iditem = ObjectId(iditem)

    # Getter
    def getitemname(self):
        return self.col_item.find_one({"_id":self.iditem})["itemname"]

    def getamountitem(self):
        return self.col_item.find_one({"_id": self.iditem})["amountitem"]

    def getprice(self):
        return self.col_item.find_one({"_id":self.iditem})["price"]

    # Setter
    def setitemname(self,newitemname):
        query = {"_id": self.iditem}
        set = {"$set":{"itemname":newitemname}}
        return self.col_item.update_one(query,set)

    def setamountitem(self,newamountitem):
        query = {"_id": self.iditem}
        set = {"$set":{"amountitem":newamountitem}}
        return self.col_item.update_one(query,set)

    def setprice(self,newprice):
        query = {"_id": self.iditem}
        set = {"$set":{"price":newprice}}
        return self.col_item.update_one(query,set)

    # Add & Delete
    def additem(self,itemname,amountitem,price):
        dict_account = {"itemname":itemname,"amountitem":amountitem,"price":price}
        return self.col_item.insert_one(dict_account)

    def delitem(self,itemname):
        query = {"itemname":itemname}
        return self.col_item.delete_one(query)

    # Method
    def addamountitem(self,amountadd):
        amountadd = int(amountadd)
        currentamount = int(self.getamountitem())
        return self.setamountitem(str(currentamount + amountadd))

    def subamountitem(self,amountsub):
        amountsub = int(amountsub)
        currentamount = int(self.getamountitem())
        return self.setamountitem(str(currentamount - amountsub))

    def getlistid(self):
        # Return List
        listid = []
        for id in self.col_item.find():
            listid.append(id["_id"])
        return listid

    def getlistdata(self):
        return self.col_item.find_one({"_id":self.iditem},{"_id":0})

    def getlistnameitem(self):
        list = []
        for name in self.col_item.find():
            list.append(name["itemname"])
        return list

    def getalldata(self):
        listdata = []
        for data in self.col_item.find({},{"_id":0}):
            listdata.append(data)
        return listdata

    def getid(self,itemname):
        data = self.col_item.find_one({"itemname":itemname})
        return data["_id"]

# a = Item()
# input = "Samsung Galaxy S20 Ultra"
# id = a.getid(input)
# b = Item(id)
# print(b.getlistdata())