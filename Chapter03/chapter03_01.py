
import os 
import sys 

a = 10 


# Ex01 
def foo():
    # read global variable
    print(f'Ex01 : {a}')


# Ex02 
def bar():
    b = 30 
    # read local variable 
    print(f'Ex02 : {b}')

foo()
bar() 

# Ex03 
c = 40 
def foobar():
    # UnboundLocal Error 
    # c = c + 10 
    # c = 10 
    # c += 100 
    print(f'Ex03 : {c}')

foobar()
# Ex04 

d = 50
def barfoo():
    global d 
    print(d)
    d = 60 
    d += 100
    print(f'Ex04 : {d}')

barfoo()

# Ex05 

def outer():
    e = 70 
    def ouput_inner():
        # nonlocal 
        nonlocal e 
        e += 10 
        print(f'Ex05 : {e}')
    return ouput_inner

in_test = outer()
in_test()
in_test()
in_test()
in_test()

# Ex06 

def func(var):
    # local variable 
    x = 10

    def printer():
        print(f'Ex06 Printer Func Inner')
    print('Func Inner', locals())

func('Hi')


# Ex07 

print(f'Ex07 {globals()}')

test_variable = 100 

print(f'Ex07 {globals()}')

# Ex08 
for i in range(1, 10):
    for k in range(1, 10):
        globals()['plus_{}_{}'.format(i, k)] = i + k 


print(globals())

print(f'Ex08 {globals()}')
