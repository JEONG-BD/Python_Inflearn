

def generator_ex1():
    print('Start')
    yield 'A point '
    print('Continue')
    yield 'B point '
    print('End')
    

if __name__ == '__main__':
    # generator ex01 
    try : 
        temp_1 = iter(generator_ex1())
        print(temp_1)
        print(next(temp_1))
        print(next(temp_1))
        print(next(temp_1))
    except StopIteration as ex : 
        print("==")

    
    for v in generator_ex1():
        print(v)
    
    # generator ex02 
    temp_2 = [x * 3 for x in generator_ex1()]
    print(temp_2)
    temp_3 = (x * 3 for x in generator_ex1())
    print(temp_3)

    for i in temp_3:
        print(i)
    