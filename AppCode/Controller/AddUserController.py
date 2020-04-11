from Models.Account import Account

class AddUserController:

    def __init__(self,username):
        self.username = username
        self.account = Account(self.username)

    # out to view
    def checkname(self):
        return self.account.getname()

    def checkrole(self):
        return self.account.getrole()

    def tabeldata(self):
        return self.account.gettabeldata()

    def checkInputDeleteAccount(self,input):
        if input == "":
            return False
        if input not in self.account.getlistusernamename():
            return False
        return True

    def deleteAccount(self,input):
        if self.checkInputDeleteAccount(input):
            self.account.delaccount(input)
            return True
        return False

    def checkInputAddAccount(self,username,password,name,role):
        if username == "":
            return False
        if password == "":
            return False
        if name == "":
            return False
        if role == "":
            return False
        if username in self.account.getlistusernamename():
            return False
        if role == "Pilih Role":
            return False
        return True

    def addAccount(self,username,password,name,role):
        if self.checkInputAddAccount(username,password,name,role):
            self.account.addaccount(username,password,name,role)
            return True
        return False


# controller = AddUserController("andri7")
# username = "andri"
# password = "123"
# name = "andri7"
# role = "Admin"
# print(controller.checkInputAddAccount(username,password,name,role))