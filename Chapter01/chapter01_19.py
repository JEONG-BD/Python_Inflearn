

if __name__ == "__main__":
    # built in functions 
    print(abs(-3))

    print(all([1, 2, 0]))
    print(any([1, 2, 0]))

    print(chr(67))
    print(ord('C'))

    for i, v in enumerate([11, 12, 13]):
        print(i, v)

    def conv_pos(x):
        return abs(x) > 2 
    
    print(list(filter(conv_pos, [1, -3, 2, 2, 0, -5, 6])))
    print(list(filter(lambda x : abs(x) >2 , [1, -3, 2, 2, 0, -5, 6])))

    print(id(int("5")))
    print(id(str(5)))

    print(max([1, 3, 2, 4, 5]))
    print(min([1, 3, 2, 4, 5]))

    def conv_abs(x):
        return abs(x)
    
    print(list(map(conv_abs, [1, -3, 2, 2, 0, -5, 6])))
    print(list(map(lambda x : abs(x), [1, -3, 2, 2, 0, -5, 6] )))
    print(pow(2, 10))
    print(list(range(1, 10, 2)))

    print(sorted([6, 7, 4, 3, 2]))
    print(sorted(['p', 'y', 't', 'h', 'o', 'n']))
    print(sum([1111, 2222, 3333]))