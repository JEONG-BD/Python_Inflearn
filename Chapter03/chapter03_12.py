
class Parent1:
    pass 

class SampleEx: 
    attr1 = 30 
    attr2 = 100 

    def add(self, m, n):
        return m + n 
    
    def mul(self, m, n):
        return m * n

if __name__ == '__main__':
    print('Type')

    s1 = type('sample1', (), {})

    print(f'Ex01 : s1 {s1}')
    print(f'Ex01 : s1 {type(s1)}')
    print(f'Ex01 : s1 {s1.__base__}')
    print(f'Ex01 : s1 {s1.__dict__}')

    print("="*6)
    s2 = type('sample2', (Parent1, ),dict(attr1=100, attr2='hi'))
    
    print(f'Ex01 : s2 {s2}')
    print(f'Ex01 : s2 {type(s2)}')
    print(f'Ex01 : s2 {s2.__base__}')
    print(f'Ex01 : s2 {s2.__dict__}')

    print("="*6)
    se = SampleEx()
    print(se.attr1)
    print(se.attr2)
    print(se.add(100, 200))
    print(se.mul(100, 200))

    print("="*6)
    s3 = type('Sample3', (object, ), dict(attr1=30, attr2=200, add=lambda x, y : x + y, mul=lambda x,y :x * y))
    print(s3.attr1)
    print(s3.attr2)
    print(s3.add(20, 200))
    print(s3.mul(20, 200))
    