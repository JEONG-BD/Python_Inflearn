

class DescriptorClass1(object):


    def __init__(self, name='Default'):
        self.name = name 


    def __get__(self, obj, objtype):
        return 'Get method called -> self : {} obj : {} objtype : {} name : {}'.format(self, obj, objtype, self.name)


    def __set__(self, obj, name):
        print('Set method called')
        if isinstance(name, str):
            self.name = name 
        else :
            raise TypeError('Name should be string')


    def __delete__(self, obj):
        print('Delete method called')
        self.name = None    

class SampleA(object):
    name = DescriptorClass1()


class DescriptorClass2(object):


    def __init__(self, value):
        self._name = value 
    

    def getVal(self):
        return 'Get method called -> self : {} name : {} '.format(self, self._name)

    def setVal(self, value):
        print('Set method called')
        if isinstance(value, str):
            self._name = value 
        else :
            raise TypeError('Name should be string')
    
    def delVal(self):
        print('Delete method called')
        self._name = None    


    name = property(getVal, setVal, delVal, 'Property Method Example')

if __name__ == '__main__':
    print('descriptor')
    s1 = SampleA()
    s1.name = 'Descriptor Test1'
    # Exception 
    # s1.name = 10 
    print(s1.name)
    del s1.name 
    print(s1.name)

    s2 = DescriptorClass2('Descriptor Test2')
    print(s2.name)
    del s2.name
    print(s2.name)
    print(DescriptorClass2.name.__doc__)