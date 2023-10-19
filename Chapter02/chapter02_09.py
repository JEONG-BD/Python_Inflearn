

if __name__ == '__main__':
    print(divmod(100, 9))
    print(divmod(* (100, 9)))
    print(*(divmod(100, 9)))

    x, y, *rest = range(10)
    print(x, y, rest)
    x, y, *rest = range(2)
    print(x, y, rest)

    # mutable, immutable 

    tu_1 = (15, 20, 25)
    lst_1 = [15, 20, 25]

    print(tu_1, id(tu_1))
    print(lst_1, id(lst_1))

    tu_1 *= 2 
    lst_1 *= 2

    print(tu_1, id(tu_1))
    print(lst_1, id(lst_1))

    # sorted , sort 
    # sorted : 정렬 후 새로운 객체 반환 
    f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawbrerry', 'coconut']
    print('sorted', sorted(f_list))
    print(f_list)
    print()

    print('sorted', sorted(f_list, reverse=True))
    print('sorted', sorted(f_list, key=len, reverse=True))
    print('sorted', sorted(f_list, key = lambda x : x[-1]))

    # sort : 정렬 후 객체 직접 변경 
    print('sort', f_list.sort(), f_list)
    print('sort', f_list.sort(reverse=True), f_list)
    print('sort', f_list.sort(reverse=True, key=len), f_list)
