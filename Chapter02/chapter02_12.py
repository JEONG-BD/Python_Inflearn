from functools import reduce, partial  
from operator import add, mul  
def factorial(n):
    '''
    NAME : Funcation Fcatorial  
    Parameter : Number n 
    CREATE DATE : 2023.10.21 
    UPDATE DATE : 2023.10.21
    CREATE USER : Admin 
    UPDATE USER : Admin 
    DESCRIPTION : Factorial 
    '''
    if n == 1 :
        return 1 
    return n * factorial(n-1)

class A : 
    '''
    NAME : Class A  
    Parameter :  
    CREATE DATE : 2023.10.21 
    UPDATE DATE : 2023.10.21
    CREATE USER : Admin 
    UPDATE USER : Admin 
    DESCRIPTION :  
    '''
    pass 

if __name__ == '__main__':
    print('first class ')
    print("====")
    print(factorial.__doc__)
    print(type(factorial))
    print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
    print(factorial.__name__)
    print(factorial.__code__)

    print()
    print()
    var_function = factorial 
    print(var_function(10))
    print(list(map(var_function, range(1, 11))))

    # map, filter, reduce 
    print([var_function(i) for i in range(1, 11) if i % 2 ])
    print(list(map(var_function, filter(lambda x : x %2, range(1, 11)))))

    # reduce 
    print(sum(range(1, 11)))
    print(reduce(add, [i for i in range(1, 11)]))

    # lambda 
    print(reduce(lambda x, t : x + t, range(1, 11)))

    # callable 
    print(callable(str))
    print(callable(A))

    #partial 
    print(mul(10, 10))
    five = partial(mul , 5)
    print(five(10))
    print([five(i) for i in range (1, 11)])

    
