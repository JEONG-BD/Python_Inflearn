import copy 

if __name__ == "__main__":
    marks1 = [['~'] * 3  for _ in range(5)]
    marks2 = [['~'] *3 ] * 4

    print(marks1)
    print(marks2)

    marks1[0][1] = 'X'
    marks2[0][1] = 'X'
    print(marks1)
    print(marks2)

    print([id(i) for i in marks1])
    print([id(i) for i in marks2])

    # mutable 

    a = [1, 2, 3]
    b = a 

    print(a, b)
    print(a == b)
    print(id(a).__eq__(id(b)))
    print(id(a), id(b))
    a[0] = 11
    print(a)
    print(b)
    b[0] = 12
    print(a)
    print(b)
 
    # immutable 

    str_a = 'abc'
    str_b = str_a
    print(str_a, str_b)
    print(str_a == str_b)
    print(id(str_a), id(str_b))
    str_b = 'abcd'
    print(id(str_a), id(str_b))

    
    # shallow copy
    print("<<<<<<shallow copy>>>>>>")
    print()
    lst_a = [1, 2, 3]
    lst_b = lst_a[:]
    print(id(lst_a), id(lst_b))
    print(lst_a, lst_b)
    print(lst_a == lst_b)
    print(lst_a is lst_b)

    print("<<<<<<shallow copy>>>>>>")
    a = [[1, 2], [3, 4]]
    b = a[:]
    print(id(a), id(b))
    print(id(a[0]), id(b[0]))
    a[0] = [5, 6]
    print(id(a[0]), id(b[0]))

    a[1].append(5)
    print(a)
    print(b)    

    sh_a = [[1, 2], [3, 4]]
    sh_b = copy.copy(sh_a)
    print(id(sh_a), id(sh_b))
    print(id(sh_a[0]), id(sh_b[0])) 


    print("<<<<<<deep copy>>>>>>")

    dp_a = [[1, 2], [3, 4]]
    dp_b = copy.deepcopy(dp_a)
    print(id(dp_a), id(dp_b))
    print(id(dp_a[0]), id(dp_b[0]))

    