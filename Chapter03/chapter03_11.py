
class SampleA(object):
    pass 

class SampleB(object):
    pass 


if __name__ == '__main__': 
    print('Meta Class')

    sa1 = SampleA()
    sa2 = SampleA()

    print(f'SampleA {sa1.__class__}')
    print(f'SampleA {type(sa1)}')
    print(f'SampleA {sa1.__class__.__class__}')
    print(f'SampleA {sa1.__class__ is type(sa1)}')
    print(f'SampleA {sa1.__class__.__class__ is type(sa1).__class__}')

    n = 10 
    dic = {'key1':20, 'key2':30}

    sa3 = SampleB()
    for o in (n, dic, sa3):
        print('SampleB {} {} {}'.format(type(o), type(o) is o.__class__, o.__class__.__class__))

    
    for t in int, float, list, tuple : 
        print(f'Test {type(t)}')