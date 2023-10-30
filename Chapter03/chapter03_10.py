from multipledispatch import dispatch

class SampleA(object):

    # def add(self, x, y):
    #     return x + y 
    
    # def add(self, x, y, z):
    #     return x + y + z 

    # def add(self, *args):
    #     return sum(args) 
    pass 

class SampleB(object):
    def add(self, datatype, *args):
        if datatype == 'int':
            return sum(args) 

        if datatype == 'str':
            return ''.join([x for x in args])

class SampleC(object):
    @dispatch(int, int)
    def product(x, y):
        return x * y 
    
    @dispatch(int, int, int)
    def product(x, y, z):
        return x * y * z 
    
    @dispatch(float, float, float)
    def product(x, y, z):
        return x * y * z 
    
if __name__ == '__main__':
    #sa = SampleA()
    #print(f'Sample A {sa.add(2, 3, 1)}')
    #print(f'Sample {dir(sa)}')
    sb = SampleB()
    print(f'SampleB {sb.add("int", 1, 3)}')
    print(f'SampleB {sb.add("str", "apple", "banana")}')

    sc = SampleC()
    print(f'SampleC {sc.product(1, 3)}')
    print(f'SampleC {sc.product(1, 3, 4)}')
    print(f'SampleC {sc.product(3.0, 4.2, 4.3)}')
    