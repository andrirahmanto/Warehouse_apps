from Models.Account import Account
from Models.Item import Item
from Models.Transaction import Transaction

class ShowAllItemController:

    def __init__(self,username):
        self.username = username
        self.item = Item()
        self.transaction = Transaction

    # out to view
    def checkname(self):
        user = Account(self.username)
        return user.getname()

    def checkrole(self):
        user = Account(self.username)
        return user.getrole()

    def tabeldata(self):
        return self.item.getalldata()