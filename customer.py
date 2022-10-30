

# class foodapp():
#     print("************food ordering************")
#     def __init__(self):
#         self.admin=1
#         self.user=2
#     def log_in(self):
#         self.log_in1=int(input("enter log in:"))
#         if self.admin==self.log_in1:
#             print("*****you are a admin***** ")           
#         elif self.user==self.log_in1:
#             print("*****you are user*****")
#         else:
#             print("enter only 1 or 2")

class food:
    def __init__(self,food_id,name,quantity,price,discount,stock):
        self.food_id=food_id
        self.name=name
        self.quantity=quantity
        self.price=price
        self.discount=discount
        self.stock=stock

    def __str__(self):
        return f" food_id :{self.food_id} \n name:{self.name} \n quantity:{self.quantity} \n price:{self.price} \n discount:{self.discount}\n stock:{self.stock}"

    def set_food_id(self,food_id):
        self.food_id = food_id

    def get_food_id(self):
        return self.food_id

    def set_name(self,name):
        self.name =name

    def get_name(self):
        return self.name

    def set_quantity(self,quantity):
        self.quantity =quantity

    def get_quantity(self):
        return self.quantity

    def set_price(self,price):
        self.price=price

    def get_price(self):
        return self.price

    def set_discount(self,discount):
        self.discount=discount

    def get_discount(self):
        return self.discount

    def set_stock(self,stock):
        self.stock=stock

    def get_stock(self):
        return self.stock 



if __name__ == "__main__":
    food_obj=food(1,"chickenroll",1,100,5,10)
    print(food_obj)