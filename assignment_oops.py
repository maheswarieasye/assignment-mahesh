


class dog:
    def __init__(self,name=None,age=0,coat=None):
        self.name=name
        self.age=age 
        self.coat=coat 

    def description(self):
        print("name:","country dog")
        print("age:",3)
        
    def set(self,coat):
        self.coat=coat

    def get(self):
        return self.coat

class JackRussellTerrier(dog):
    def dog_name():
        print("name:","jack")
    def age():
        print("age:",5)

class bulldog(dog):
    def dog_name():
        print("name:","bull")        
    def age():
        print("age:",6)
        
        

# obj=dog("country dog",3)
# obj.description()
# obj.set("white")
# print(obj.get())

obj=JackRussellTerrier()
JackRussellTerrier.dog_name()
JackRussellTerrier.age()

obj=bulldog()
bulldog.dog_name()
bulldog.age()

obj.description()
obj.set("white")
print(obj.get())







