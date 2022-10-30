
from customer import food

class food_items:

    foodlist=[]
    def log_in(self):
        self.log_in_no=int("enter the value")

    def add_fooditems(self):
        print("*****ADD FOODITEMS*****")
        food_id=int(input("enter the food_id:"))
        name=input("enter the food name:")
        quantity=(input("enter the quantity:"))
        price=int(input("enter the price"))
        discount=int(input("enter the discount"))
        stock=int(input("enter the stock"))
        obj=food(food_id,name,quantity,price,discount,stock)
        self.foodlist.append(obj)

    def view(self):
        print("*********view list*******")
        for foods in self.foodlist:
            print(foods,"\n")

    def search(self,food_id):
        for foods in self.foodlist:
            if foods.get_food_id() == food_id:
                return foods
        print("No such food_id Found!!")
        return

    def delete(self):
        print("*******Delete******")
        try:
            food_id = int(input("Enter food ID : "))
            food= self.search(food_id)
            if food:
                self.foodlist.remove(food)
                print("Successfully Deleted")
        except Exception as ex:
            print(ex)
  
    def update(self):
        print("*******Update food*******")
        food_id= int(input("Enter food id : "))
        food= self.search(food_id)
        if food:
            name = input("Enter food name : ")
            quantity = int(input("Enter quantity : "))
            price = int(input("Enter price : "))
            discount = input("Enter discount : ")
            stock = int(input("Enter stock : "))

            food.set_name(name)
            food.set_quantity(quantity)
            food.set_price(price)
            food.set_discount(discount)
            food.set_stock(stock)

            print("Successfully Updated")

