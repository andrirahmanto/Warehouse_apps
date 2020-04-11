from Models.Account import Account
from Models.Item import Item

class HomeManagerItemController:

    def __init__(self,username):
        self.username = username
        self.account = Account(self.username)
        self.item = Item()

    # out to view
    def checkname(self):
        return self.account.getname()

    def checkrole(self):
        return self.account.getrole()

    def tabeldata(self):
        return self.item.getalldata()

    def getallnameitem(self):
        return self.item.getlistnameitem()

    def checkinputAddAmountItem(self,itemname,amountitem):
        try:
            if itemname == "Pilih Barang":
                return False
            if amountitem == '':
                return False
            item = Item()
            id = item.getid(itemname)
            item = Item(id)
            if int(amountitem)<0:
                return False
            return True
        except:
            return False

    def AddAmountItem(self,itemname,amountitem):
        if self.checkinputAddAmountItem(itemname,amountitem):
            item = Item()
            id = item.getid(itemname)
            item = Item(id)
            item.addamountitem(amountitem)
            return True
        return False

    def checkInputAddItem(self,itemname,price,amountitem):
        if itemname == '':
            return False
        if price == '':
            return False
        if not self.checkinputmustbeinteger(price):
            return False
        if amountitem == '':
            return False
        if not self.checkinputmustbeinteger(amountitem):
            return False
        if itemname in self.item.getlistnameitem():
            return False
        return True

    def checkinputmustbeinteger(self,input):
        try:
            input = int(input)
            return True
        except:
            return False

    def AddItem(self,itemname,price,amountitem):
        if self.checkInputAddItem(itemname,price,amountitem):
            self.item.additem(itemname,price,amountitem)
            return True
        return False


