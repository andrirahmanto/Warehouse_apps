from Models.Account import Account
from Models.Transaction import Transaction

class ShowTransactionController:

    def __init__(self,username):
        self.username = username
        self.account = Account(username)
        self.transaction = Transaction()

    # out to view
    def checkname(self):
        return self.account.getname()

    def checkrole(self):
        return self.account.getrole()

    def tabeldata(self):
        return self.transaction.gettabeldata()
