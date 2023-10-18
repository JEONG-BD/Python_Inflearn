import array 

if __name__ == "__main__":
    print('sequence')
    print('comprehending list')
    chars = '+_)(*&^%$#@!)'
    code_list1 = []

    for s in chars : 
        # unicode 
        code_list1.append(ord(s))
    print(code_list1)

    code_list2 = [ord(s) for s in chars]
    print(code_list2)

    code_list3 = [ord(s) for s in chars if ord(s) > 40]
    print(code_list3)

    code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
    print(code_list4)


    print([chr(s) for s in code_list1])

    # generator 
    tuple_1 = [ord(s) for s in chars]
    tuple_2 = (ord(s) for s in chars)
    print(tuple_1)
    print(type(tuple_2))
    # print(next(tuple_2))
    # print(next(tuple_2))
    # print(next(tuple_2))
    # print(next(tuple_2))

    array_g = array.array('I', (ord(s) for s in chars))
    print(array_g)
    print(type(array_g))
    print(array_g.tolist())

    print('%s' %c + str(n) for c in 'A B C D'.split() for n in range(1, 21))

    for s in ('%s' %c + str(n) for c in 'A B C D'.split() for n in range(1, 21)):
        print(s)
