from admin import food_items


class main:
    def __init__(self):
        self.food_items= food_items()

    def execute(self,choice):
        if choice == 1:
            self.food_items.add_fooditems()
        elif choice == 2:
            self.food_items.view()
        elif choice == 3:
            food_id = int(input("Enter food id : "))
            food = self.food_items.search(food_id)
            print(food)
        elif choice == 4:
            self.food_items.delete()
        elif choice == 5:
            self.food_items.update()
        
if __name__ == "__main__":
    
    obj = main()

    while True:
        choice = int(input("Enter \n1.Addfood \n2.View food \n3.Search food \n4.Deletefood \n5.Update food : \n"))
        if choice > 5 or choice < 1:
            break
        obj.execute(choice)