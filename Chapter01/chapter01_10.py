

if __name__ == "__main__":
    # for 
    for v1 in range(10):
        print('v1 is =', v1)
    
    for v2 in range(1, 11):
        print('v2 is =', v2)
    
    for v3 in range(1, 11, 2):
        print('v3 is = ', v3)

    sum_ = 0
    for v4 in range(1, 1001):
        sum_ += v4
    print(sum_)

    print(sum(range(1, 1001)))
    print(sum(range(1, 1001, 4)))

    # Iterable 
    # string, list, tuple, dictionary 

    names = ['Lee', 'Kim', 'Park', 'Jeong', 'You']

    for v in range(len(names)):
        print(names[v])

    lotto_numbers = [11, 19, 21, 28, 36, 37]

    for v in lotto_numbers:
        print(v)

    
    for v in 'word':
        print(v)

    
    dic_ = {"Name":"Lee", "Age":20, "City":"Seoul"}

    for v in dic_:
        print(v)

    for k, v in dic_.items():
        print(k, v)

    for v in dic_.values():
        print(v)

    names = 'FineAppLE'

    for n in names:
        if n.isupper():
            print(n)
        else :
            print(n.upper())
    
    # break 

    numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 28]

    for v in numbers :
        if v == 34 :
            print("Found ! ", v )
            break
        else : 
            print("Not found ! ")

    # continue 
    
    lt = ['1', 2, 5, True, 4.3, complex(4)]

    for v in lt : 
        if type(v) is bool :
            print(v,)
            continue
        print(type(v))

    # for else 


    numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 28]

    for v in numbers :
        if v == 24 :
            print('Found 24')
            break
    else :
        print('Not found')

    
    for row in range(2, 10):
        for col in range(1, 10):
            print(row ,"*", col , "=",  row *col)
        print()

    
    name2 = 'Aceman'
    print("Reversed", reversed(name2))
    print("Reversed list", list(reversed(name2)))
    print("Reversed tuple", tuple(reversed(name2)))
    print("Reversed set", set(reversed(name2)))