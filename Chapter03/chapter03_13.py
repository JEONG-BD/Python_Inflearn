
def  cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d

def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new 


class MetaClassName(type):

    #def __new__(metacls, name, base, namespace):
    #    pass

    def __init__(self, object_or_name, bases, dict):
        print('__init__ -> ', self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases, dict)
    
    def __call__(self, *args, **kwargs):
        print('__call__ -> ', self, *args, **kwargs)
        return super().__call__(*args, **kwargs)

    def __new__(metacls, name, bases, namespace):
        print('__new__ -> ', metacls, name, bases, namespace)
        namespace['desc'] = 'custom list'
        namespace['cus_mul'] = cus_mul
        namespace['cus_replace'] = cus_replace
        return type.__new__(metacls, name, bases, namespace)        
if  __name__ == '__main__':
    print('Type')

    CustomList = type('CustomList1', (list, ), {'desc':'custom list', 'cus_mul':cus_mul, 'cus_replace':cus_replace})

    c1 = CustomList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    c1.cus_mul(15)
    print(f'Ex1 > {c1}')

    c1.cus_replace(15, 7777)
    print(f'Ex1 > {c1}')
    print(f'Ex1 > {c1.desc}')
    print('='*6)

    print('='*6)
    CustomList2 = MetaClassName('CustomList2', (list, ), {})
    
    c2 = CustomList2([1, 2, 3, 4, 5, 6, 7, 8, 9])
    c2.cus_mul(1000)
    c2.cus_replace(1000, 7777)
    print(f'Ex2 > {c2}')
    print(f'Ex2 > {c2.desc}')
        
    