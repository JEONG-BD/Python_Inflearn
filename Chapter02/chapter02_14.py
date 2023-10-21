import traceback

def closure_ex1():
    # free variable 
    # closure area 
    series = []

    def averager(v):
        series.append(v)
        print('inner >> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    
    return averager

def closure_ex2():
    try : 

        cnt = 0 
        total = 0

        def averager(v):
            nonlocal cnt, total 
            cnt += 1 
            total += v 
            return total / cnt 
        return averager

    except Exception as ex:
        print(traceback.format_exc())

if __name__ == '__main__':
    avg_closure1 = closure_ex1()
    print(avg_closure1)
    print(avg_closure1(10))
    print(avg_closure1(20))
    print(avg_closure1(30))
    print(dir(avg_closure1.__code__))
    print(avg_closure1.__code__.co_freevars)
    print(avg_closure1.__closure__[0].cell_contents)


    avg_closure2 = closure_ex2()
    print(avg_closure2(10))
    print(avg_closure2(20))
    print(avg_closure2(30))
