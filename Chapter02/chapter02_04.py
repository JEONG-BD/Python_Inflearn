
class Fruit:
    def __init__(self, name, price): 
        self._name = name 
        self._price = price 
    
    def __str__(self):
        return 'Fruit Class Info {} {}'.format(self._name, self._price)
    
    def __add__(self, x):
        print('Called __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('Called __sub__')
        return self._price - x._price 
    
    def __le__(self, x):
        print('Called __le__')
        if self._price <= x._price :
            return True 
        else :
            return False 
    
    def __ge__(self, x):
        print('Called __ge__')
        if self._price >= x._price:
            return True 
        else :
            return False 

if __name__ == "__main__":
    print("special method(magic method)")
    print(type(int))
    n = 10 
    print(n + 10)
    print(n.__add__(10))
    print(n.__doc__)
    print(n.__bool__(), bool(n))

    s1 = Fruit('Apple', 3000)
    s2 = Fruit('Banana', 4500)
    print(s1._price + s2._price)
    print(s1.__add__(s2))
    print(s1 + s2)

    print(s1.__sub__(s2))

    print(s1.__le__(s2))
    print(s1.__ge__(s2))