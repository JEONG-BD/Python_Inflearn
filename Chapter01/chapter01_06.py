
if __name__ == "__main__":
    # tuple 
    tup_a = ()
    tup_b = (1, )
    tup_c = (11, 12, 13 ,14)
    tup_d = (100, 1000, 'ACE', 'Base', 'Captine')
    tup_e = (100, 1000, ('ACE', 'Base', 'Captine'))
    
    print(type(tup_a))
    print(type(tup_b))
    print(tup_d[1])
    print(tup_d[0] + tup_d[1], +tup_d[1])
    print(tup_e[-1])
    print(tup_e[-1][1])
    print(list(tup_e[-1][1]))

    # slicing 
    print(tup_d[0:3])
    print(tup_e[2:])
    print(tup_e[2][1:3])

    # operator 
    print(tup_c + tup_d)
    print(tup_c * 3)

    # function 
    a = (5, 2, 3, 1, 4)
    print(a)
    print(a.index(3))
    print(a.count(2))

    #packing unpacking 
    t = ('foo', 'bar', 'baz', 'qux')
    print(t)

    (x1, x2, x3, x4) = t 
    print(x1, type(x1))
    print(x2, type(x2))
    print(x3, type(x3))
    print(x4, type(x4))

    t2 = 1, 2, 3 
    print(type(t2))
    t3 = (4, )
    print(type(t3))

    a1, a2, a3 =t2 
    print(a1)
    print(a2)
    print(a3)
