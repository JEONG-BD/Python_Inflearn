import itertools 

if __name__ == '__main__':
    # count 
    gen1 = itertools.count(1, 2.5)
    print(next(gen1))
    print(next(gen1))

    # takewhile 
    gen2 = itertools.takewhile(lambda x : x < 10000, itertools.count(1, 2.5))

    for i in gen2 :
        print(i)

    # filterfalse 

    gen3 = itertools.filterfalse(lambda x : x < 3 , [1, 2, 3, 4, 5])
    
    for i in gen3:
        print(i)

    gen4 = itertools.accumulate([x for x in range(1, 101)])
    print(gen4)
    for i in gen4 :
        print(i)

    # chain 
    gen5 = itertools.chain('ABCDEF', range(1, 11, 2))
    for i in gen5 :
        print(i)

    # chain 
    gen6 = itertools.chain(enumerate('ABCDE'))
    print(list(gen6))


    # product 
    gen7 = itertools.product('ABCDEF')
    for i in gen7 :
        print(i)
    
    gen8 = itertools.product('ABCD', repeat=4)
    for i in gen8 :
        print(i)
    
    # groupby 

    gen9 = itertools.groupby('AAAABBBCCDDEEEE')

    for chr, group in gen9 :
        print(chr, ':', list(group))