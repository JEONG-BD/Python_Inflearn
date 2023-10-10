if __name__ == "__main__":
    # while 

    n = 5 
    while n > 0 :
        n = n - 1
        print(n)

    a = ['foo', 'bar', 'baz']

    while a : 
        print(a.pop(-1))

    n = 5 

    while n > 0 : 
        n -= 1 
        if n == 2 :
            break 
        print(n)
    print("Loop Ended")

    while n > 0 :
        n -= 1 
        if n == 2 :
            continue 
        print(n)
    print("Loop Ended")

    i = 1 

    while i <= 10:
        i += 1 
        if i == 6 :
            break 
        print(i)

    n = 10 
    while n > 0 :
        n -= 1 
        print(n)
        if n == 5 :
            break 
    else :
        print("else out")

    
    a = ['foo', 'bar', 'baz', 'qux']
    s = 'qux'
    i = 0 

    while i < len(a):
        print(a[i])
        if a[i] == s:
            print(a[i])
            break 
        i+= 1 

    else :
        print(s, 'not found in list')