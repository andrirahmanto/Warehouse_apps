from Models.Account import Account
from Models.Item import Item
from Models.Transaction import Transaction

class HomeCashierController:

    def __init__(self,username):
        self.username = username
        self.account = Account(self.username)
        self.item = Item()
        self.transaction = Transaction()

    # out to view
    def checkname(self):
        return self.account.getname()

    def checkrole(self):
        return self.account.getrole()

    def tabeldata(self):
        return self.item.getalldata()

    def getallnameitem(self):
        return self.item.getlistnameitem()

    def checkInputMustBeInteger(self,input):
        try:
            input = int(input)
            return True
        except:
            return False

    def checkInput(self,itemname,amountitem):
        if itemname == "Pilih Barang":
            return False
        if amountitem == '':
            return False
        if not self.checkInputMustBeInteger(amountitem):
            return False
        item = Item()
        id = item.getid(itemname)
        item = Item(id)
        if int(amountitem) > int(item.getamountitem()):
            return False
        return True

    def subAmountitem(self,itemname,amountitem):
        if self.checkInput(itemname,amountitem):
            item = Item()
            id = item.getid(itemname)
            item = Item(id)
            item.subamountitem(amountitem)
            self.AddTransaction(itemname,amountitem)
            return True
        return False

    def gettotalprice(self,itemname,amountitem):
        item = Item()
        id = item.getid(itemname)
        item = Item(id)
        price = item.getprice()
        totalprice = int(price)*int(amountitem)
        return str(totalprice)

    def AddTransaction(self,itemname,amountitem):
        cashiername = self.username
        item = Item()
        id = item.getid(itemname)
        item = Item(id)
        itemname = item.getitemname()
        price = item.getprice()
        amountitem = amountitem
        totalprice = self.gettotalprice(itemname,amountitem)
        self.transaction.addtransaction(cashiername,itemname,amountitem,price,totalprice)




