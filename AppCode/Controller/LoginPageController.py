from Models.Account import Account

class LoginPageController:

    def __init__(self,username,password):
        self.username = username
        self.password = password


    def checklogin(self):
        user = Account(self.username)
        password = user.getpassword()
        if self.password == password:
            return True
        return False

    def checkrole(self):
        user = Account(self.username)
        return user.getrole()
