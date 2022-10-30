from ast import MatchSequence
from delivery import user

class profile:
    add_details=[]
    def __init__(self):
        print("****enter the details****")
        fullname=input("enter the fullname:")
        phoneno=int(input("enter the phoneno:"))
        email=input("enter the email:")
        address=input("enter the address:")
        password=input("enter the password")
        obj1=user(fullname,phoneno,email,address,password)
        self.add_details.append(obj1)

    def log_in(self):
        print("****log_in details****")
        for user in self.add_details:
            if user.get_email==input("enter the email:") :
                user.get_password==input("enter password:")
                print("your are log_in and enter the menu")
        else:
            print("enter the correct email/password")

    def search(self,fullname):
        for user in self.add_details:
            if user.get_fullname() == fullname:
                return user
        print("No such name Found!!")
        return

    def update(self):
        print("*******Update profile*******")
        fullname= input("Enter fullname : ")
        user= self.search(fullname)
        if user:
            phoneno= input("Enter fullname : ")
            email= (input("Enter email: "))
            address = (input("Enter address : "))
            password = input("Enter password : ")

            user.set_phoneno(phoneno)
            user.set_email(email)
            user.set_address(address)
            user.set_password(password)
            print("Successfully Updated")
obj3=profile()
obj3.log_in()
obj3.update()