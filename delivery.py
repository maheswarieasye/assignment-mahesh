class user:
    def __init__(self,fullname,phoneno,email,address,password):
        self.fullname=fullname
        self.phoneno=phoneno
        self.email=email
        self.address=address
        self.password=password

    def __str__(self):
        return f"fullname:{self.fullname} \nphoneno:{self.phoneno} \nemail:{self.email} \naddress:{self.address} \npassword:{self.password}"

    def set_fullname(self,fullname):
        self.fullname=fullname

    def get_fullname(self):
        return self.fullname

    def set_phoneno(self,phoneno):
        self.phoneno=phoneno

    def get_phoneno(self):
        return self.phoneno

    def set_email(self,email):
        self.email=email

    def get_email(self):
        return self.email

    def set_address(self,address):
        self.address=address

    def get_address(self):
        return self.address

    def set_password(self,password):
        self.password=password

    def get_password(self):
        return self.password

if __name__=="__main__":
    user_obj=user("mahesh",1234567890,"mahes@gmail.com","chennai","M@hesh17")
    print(user_obj)