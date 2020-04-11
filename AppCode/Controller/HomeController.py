from Models.Account import Account

class HomeController:

    def __init__(self,username):
        self.username = username

    # out to view
    def checkname(self):
        user = Account(self.username)
        return user.getname()

    def checkrole(self):
        user = Account(self.username)
        return user.getrole()