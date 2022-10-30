from delivery1 import profile


class main:
    def __init__(self):
        self.profile= profile()

    def execute(self,choice):

        if choice == 1:
            self.add_details.add()
        elif choice == 2:
            self.add_details.log_in()
        elif choice == 3:
            fullname = int(input("Enter fullname: "))
            user = self.add_details.search(fullname)
            print(user)
        elif choice == 4:
            self.add_details.update()
        
if __name__ == "__main__":
    
    obj = main()

    while True:
        choice = int(input("Enter \n1.Add \n2.log_in \n3.Search  \n4.Update food : \n"))
        if choice > 4 or choice < 1:
            break
        obj.execute(choice)