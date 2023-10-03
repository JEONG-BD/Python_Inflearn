import math 


if __name__ == "__main__":
    print("int")
    # int 
    # float 
    # complex 
    # bool 
    # str (Sequence)
    # list (Sequence)
    # tuple (Sequence)
    # set 
    # dict 

    # data type 
    str1 = "Python"
    bool = True 
    str2 = "Anaconda"
    float_v = 10.0 
    int_v = 7 

    list = [str1, str2]
    print(list)

    dict = {
        "name" : "Machine Learning", 
        "version" : 2.0
        }

    tuple = (7, 8, 9)
    set = {7, 8, 9}
    print(dict)
    print(type(str1))
    print(type(bool))
    print(type(str2))
    print(type(float_v))
    print(type(int_v))
    print(type(tuple))
    print(type(set))

    # int operator 
    i = 77 
    i2 = -14 
    big_int = 77777777777779999999999999 

    print(i)
    print(i2)
    print(big_int)

    f1 = 0.9999
    f2 = 3.141592 
    f3 = -3.9 
    f4 = 3/9 

    i1 = 39 
    i2 = 939 
    big_int1 = 7777777777
    big_int2 = 3424342424

    print(">>>>+")
    print(f"i1 + i2 = {i1 + i2}") 
    print(f"f1 + f2 = {f1 + f2}") 
    print(f"big_int1 + big_int2 = {big_int1 + big_int2}") 
       
    
    print(">>>>*")
    print(f"i1 * i2 = {i1 * i2}") 
    print(f"f1 * f2 = {f1 * f2}") 
    print(f"big_int1 * big_int2 = {big_int1 * big_int2}") 

    # type casting 
    a = 3.
    b = 6 
    c = .7
    d = 12.7 

    print(type(a)) 
    print(type(b)) 
    print(type(c)) 
    print(type(d))

    print(float(d))
    print(int(c))
    print(int(d))

    print(int(True))
    print(float(False))

    print(abs(-7))
    x, y = divmod(100, 8)
    print(x, y)
    print(pow(5, 3))
    print(5**3)

    print(math.pi)
    print(math.ceil(5.1))