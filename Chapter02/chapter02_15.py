import time 

def perf_clock(func):
    def perf_clocked(*args):
        st = time.perf_counter()

        result = func(*args)

        et = time.perf_counter() - st

        name = func.__name__ 

        arg_str = ','.join(repr(arg) for arg in args)

        print('[%0.5fs] %s(%s) -> %r' %(et, name, arg_str, result))
        return result 
    
    return perf_clocked

@perf_clock
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)

if __name__ == "__main__":
    print('decorator')
    print(time_func(1))    
    none_deco1 = perf_clock(time_func)
    none_deco2 = perf_clock(sum_func)
    print(none_deco1, none_deco1.__code__.co_freevars)
    print(none_deco2, none_deco2.__code__.co_cellvars)
    print('*' *40 , 'Called None Decorator --> time_func')
    print()
    none_deco1(1.5)
    print()
    print()
    none_deco2(100, 200, 300, 400, 500)
    print('*' *40 , 'Called None Decorator --> sum_func')
    
