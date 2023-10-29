# Access Modifier(Naming Mangling) 
# name : public 
# _name : protected 
# __name : private 

# No use Property 

class SampleA(object):
    def __init__(self):
        self.x = 0 
        self.__y = 0
        self._z = 0 

class SampleB:
    def __init__(self):
        self.x = 0 
        self.__y = 0 
        self._z = 0 

    def get_y(self):
        return self.__y 
    
    def set_y(self, value):
        self.__y = value
if __name__ == '__main__':
    print('property')
    print('underscore')

    x, _, y = (1, 2, 3)
    print(x, y) 
    x, *_, y = (1, 2, 3, 4, 5)
    print(x, y)

    for _ in range(10):
        print('Hello')
    
    for _, val in enumerate(reversed(range(10))):
        print(val)
    

    a = SampleA()
    a.x = 1 
    print('Ex01 > x : {}'.format(a.x))
    # print('Ex02 > y : {}'.format(a.__y))
    print('Ex01 > z : {}'.format(a._z))
    print('Ex01 > dir(a) : {}'.format(dir(a)))
    a._SampleA__y = 2
    print('Ex01 > y : {}'.format(a._SampleA__y))


    b = SampleB()
    b.x = 1 
    b.set_y(2)
    print(b.get_y())
    print(dir(b))

