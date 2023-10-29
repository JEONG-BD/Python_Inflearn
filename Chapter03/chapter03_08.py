

class SampleA(object):

    def __init__(self):
        self.x = 0 
        self.__y = 0 
    
    @property
    def y(self):
        print(f'Called get method')
        return self.__y 
    
    @y.setter
    def y(self, value):
        print(f'Called set method')
        self.__y = value
    
    @y.deleter
    def y(self):
        del self.__y 

class SampleB(object):

    def __init__(self):
        self.x = 0 
        self.__y = 0 
    
    @property
    def y(self):
        return self.__y 
    
    @y.setter
    def y(self, value):
        if value < 0 :
            raise ValueError('value < 0 ')
        self.__y = value
    
    @y.deleter
    def y(self):
        del self.__y 


if __name__ == '__main__':
    print('setter', 'getter')

    a = SampleA()
    print('Ex01 > : {}'.format(dir(a)))
    a.x =1 
    a.y =2 
    print('Ex01 > : x : {}'.format(a.x))
    print('Ex01 > : y : {}'.format(a.y))

    del a.y 
    print('Ex01 > : {}'.format(dir(a)))

    b = SampleB()
    b.x = 1 
    b.y = -2 
    print(b.y)