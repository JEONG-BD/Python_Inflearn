if __name__ == "__main__":
    # list 
    list_a = []
    list_b = list()
    list_c = [70, 75, 80, 85]
    print(type(list_a))
    list_d = [1000, 10000, 'ACE', 'Base', 'Captine']
    list_e = [1000, 10000, ['ACE', 'Base', 'Captine']]
    list_f = [21.42, 'foobar', 3, 4, False, 3.141592]

    print('>>>>>>')
    print(type(list_d))
    print(list_d[1])
    print(list_d[0] + list_d[1] + list_d[1])
    print(list_d[-1])
    print(list_e[-1][1])
    print(type(list_e[-1][1]))
    print(list(list_e[-1][1]))

    # slicing
    print(list_d[0:3])
    print(list_d[2:])
    print(list_e[-1][1:3]) 

    # list operator 
    print(">>>>>>")
    print(list_c + list_d)
    print(list_c * 3)
    print("Test + " + str(list_c[0]))

    print(list_c == list_c[:3] + list_c[3:])

    # identity 
    temp = list_c 
    print(temp)
    print(id(temp))
    print(id(list_c))
    
    print(">>>>>>")
    list_c[0] = 4 
    print(list_c)
    list_c[1:2] = ['a', 'd', 'c']
    # list_c[1:2] = [['a', 'd', 'c']]
    print(list_c)
    list_c[1:3] = []
    print(list_c)
    del(list_c[2])
    print(list_c)

    # function 
    list_g = [5, 2, 3, 1, 4]
    print(list_g)

    list_g.append(10)
    print(list_g)

    list_g.sort()
    print(list_g)

    list_g.reverse()
    print(list_g)

    print(list_g.index(3))

    list_g.insert(2, 7)
    print(list_g)

    list_g.reverse()
    print(list_g)

    list_g.remove(10)
    print(list_g)

    list_g.pop()
    print(list_g)

    list_g.pop()
    print(list_g)

    print(list_g.count(4))

    list_ex =[8, 9]
    list_g.extend(list_ex)
    print(list_g)

    while list_g:
        data = list_g.pop()
        print(data)
    




