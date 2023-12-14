Accounts={}



class User:

    def __init__(self,name,ID):
        self.name = name
        self.ID = ID

    def set_age(self,age):
        self.age = age



class LoginAccount:
    def __init__(self,Email,Password):
        self.Email=Email
        self.Password=Password
        Accounts[Email]=Password


    def existsss(self):
        if self.Email in Accounts:
            print('account exists')
        else:
            print('account does not exist!')

    
Tom = User('Tom','123')
Tom.ID = 321
Tom.set_age(20)

print(Tom.age)
print(Tom.name)
print(Tom.ID)
Eric = LoginAccount('gmaiol@gmail',123123123)
Eric.existsss()
Susie = LoginAccount('hanamail@hanamail',90909090)
print(Accounts)

