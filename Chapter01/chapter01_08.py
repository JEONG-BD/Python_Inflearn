if __name__ == "__main__":
    # set 
    set_a = set() 
    set_b = set([1, 2, 3, 4])
    set_c = set([1, 4, 5, 6])
    set_d = set([1, 2, 3, 'Pen', 'Cap', 'Plate'])
    set_e = {'foo', 'bar', 'baz', 'foo', 'qux'}
    set_f = {42, 'foo', (1, 2, 3), 3.141592}
    print(type(set_a), set_a)
    print(type(set_b), set_b)
    print(type(set_c), set_c)
    print(type(set_d), set_d)
    print(type(set_e), set_e)
    print(type(set_f), set_f)

    # set -> tuple 
    t = tuple(set_b)
    print(t, type(t))

    l = list(set_c)
    print(l, type(l))

    s1 = set([1, 2, 3, 4, 5, 6])
    s2 = set([4, 5, 6, 7, 8, 9])

    print(s1 & s2)
    print(s1.intersection(s2))

    print(s1 | s2 )
    print(s1.union(s2))

    print(s1 - s2) 
    print(s1.difference(s2))
    
    print(s1.isdisjoint(s2))
    print(s1.issubset(s2))
    print(s1.issuperset(s2))

    s1 = set([1, 2, 3, 4,])
    s1.add(5)
    print(s1)
    s1.remove(2)
    print(s1)

    s1.discard(2)
    print(s1)