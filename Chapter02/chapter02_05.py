
# class Fruit:
#     def __init__(self, name, price):
#         self._name = name 
#         self._price = price 
    
#     def __str__(self):
#         return f"Fruit class Info {self._name} {self._price} "

#     def __add__(self, x):
#         return self._price + x._price 
    
#     def __sub__(self, x):
#         return self._price - x._price 
    
#     def __le__(self,  x):
        
#         if self._price <= x._price :
#             return True 
#         else :
#             return False 
    
#     def __ge__(self, x):
#         if self._price >= x._price :
#             return True 
#         else :
#             return False
class Vector(object):
    """
    *************************
    NAME   : Vector Class 
    AUTHOR : Admin 
    CREATE DATE : 2023.10.18
    UPDATE DATE : 2023.10.18
    DESCRIPTION : 
    *************************  
    """

    def __init__(self, *args):
        '''
        Create a vector, example : v = Vector(5, 10)
        '''    
        if len(args) == 0 :
            self._x ,self._y = 0, 0 
        else : 
            self._x , self._y = args 
    
    def __repr__(self):
        '''
        Return the vector informations 
        '''
        return 'Vector(%r, %r)' %(self._x, self._y)
    
    def __add__(self, other):
        '''
        Return the vector addition of self and other 
        '''
        return Vector(self._x + other._x, self._y + other._y)
    
    
    def __mul__(self, y):
        return Vector(self._x *y , self._y * y )
    
    def __bool__(self):
        return bool(max(self._x , self._y))
    
if __name__ == "__main__": 
   print(Vector.__init__.__doc__)

   v1 = Vector(2, 3)
   v2 = Vector(23, 35)
   v3 = Vector()
   print(v1)
   print(v3)

   print(Vector.__add__.__doc__)
   print(v1 + v2)
   print(v1 * 3)
   print(v2 * 10)
   print(bool(v1))