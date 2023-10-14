
class Dog:
    species = "first_dog"

    def __init__(self, name, age):
        self.name = name 
        self.age = age 

class SelfTest:
    def func1():
        print("Called Func1")
    def func2(self):
        print("Called Func2")

class Cat : 
    species = "first_cat"

    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    def info(self):
        return "{} is {} years old".format(self.name, self.age)
    
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)
    

class Warehouse:
    stock_num = 0 

    def __init__(self, name):
        self.name = name 
        Warehouse.stock_num += 1 
    
    def __del__(self):
        Warehouse.stock_num -= 1 

if __name__ == "__main__":
    print("class")
    dog_1 = Dog("baby_1", "1")
    dog_2 = Dog("baby_2", "3")
    # namespace 
    print(dog_1 == dog_2, id(dog_1), id(dog_2))    
    print(dog_1.__dict__)
    print(dog_2.__dict__)

    print(dog_1.age)
    print(dog_1.name)
    print(dog_1.species)
    
    # self 
    f = SelfTest()
    print(dir(f))
    print(id(f))
    f.func2()

    user1 = Warehouse("Lee")
    user2 = Warehouse("Jeong")
    print(Warehouse.stock_num)

    cat_1 = Cat("first", 10)
    cat_2 = Cat("second", 22)
    print(cat_1.info())
    print(cat_1.speak("Meow"))