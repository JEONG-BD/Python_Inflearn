from functools import reduce 


def also_squre(nums):
    def double(x):
        return x ** 2 
    return map(double, nums)

def also_event(nums):
    def is_even(x):
        return x % 2 == 0 
    return filter(is_even, nums)

def also_add(nums):
    def add_plus(x, y):
        return x + y 
    return reduce(add_plus, nums)

if __name__ == '__main__':
    
    # Map 

    # Ex01
    cul = lambda a, b, c, : a * b +c 
    print(cul(10, 20, 30))

    # Ex02 
    digit = [x * 10 for x in range(1, 11)]
    print(digit)
    result = list(map(lambda x : x ** 2, [1, 2, 3, 4, 5]))
    print(result)

    # Ex03 
    print(list(also_squre(digit)))

    # Reduce 
    digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(filter(lambda x : x % 2 ==0, digit )))
    print(list(also_event(digit)))

    digit = [x for x in range(1, 101)]
    print(digit)

    result =reduce(lambda x, y : x + y , digit)
    print(result)
    print(also_add(digit))