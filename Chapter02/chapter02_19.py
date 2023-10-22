from inspect import getgeneratorstate

def coroutine1():
    print('coroutine started')
    i = yield 
    print('>>>> coroutine received : {}'.format(i))

def coroutine2(x):
    print('coroutine started : {}'.format(x))
    y = yield x 
    print('coroutine received : {}'.format(y))
    z = yield x + y 
    print('coroutine received : {}'.format(z))

def generator1():
    for x in 'AB':
        yield x 
    
    for y in range(1, 4):
        yield y 

def generator2():
    yield from 'AB'
    yield from range(1, 4)

if __name__ == '__main__':
    print('Coroutine')

    cr1 = coroutine1()
    print(cr1, type(cr1))
    next(cr1)

    # cr1.send(100)

    # GEN_CREATED : 처음 대기 상태 
    # GEN_RUNNING : 실행 상태 
    # GEN_SUSPENDED : yield 대기 상태 
    # GEN_CLOSED : 실행 완료 상태 

    cr3 = coroutine2(10)
    print(getgeneratorstate(cr3))
    print(getgeneratorstate(cr3))
    print(next(cr3))
    print(cr3.send(300))
    print(getgeneratorstate(cr3))
    print()
    print()

    t1 = generator1()
    
    for i in t1 :
        print(i) 

    t2 = generator2()

    for i in t2:
        print(i)