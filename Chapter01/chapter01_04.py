
if __name__ == "__main__":
    str1 = "I am Python"
    str2 = "Python"
    str3 = "How are you"
    str4 = "Thank you"

    print(type(str1), type(str2), type(str3), type(str4))
    print(len(str1), len(str2), len(str3), len(str4))

    str1_t1 = ''
    str2_t2 = str()
    print(type(str1_t1), type(str2_t2))
    print(len(str1_t1), len(str2_t2))

    print("I'm boy")
    print('I\'m boy')
    print('a \t b')
    print('a \n b')
    print('a \"\" b')

    escape_str1 = "Do you have a \"retro games\" ?"
    print(escape_str1)
    escape_str2 = "What\'s on Tv"
    print(escape_str2)

    t_s1 = "Click \t Start!"
    t_s2 = "New line \nCheck!"
    print(t_s1)
    print(t_s2)

    # Raw String 
    r_s1 = r'D:\Python\test'
    print(r_s1)
    
    # Multi line input
    multi_str = \
    """
    string 
    multi line 
    test 
    """
    print(multi_str)

    # string operator 
    o_str1 = "Python"
    o_str2 = "Apple"
    o_str3 = "How are you doing"
    o_str4 = "Seoul Daejeon Busan Jeju"
    print(o_str1 * 3)
    print(o_str1 + o_str2)
    print('y' in o_str1)
    print('z' in o_str2)
    print('P' not in o_str2)

    # string casting 
    print(str(66), type(str(66)))
    print((str(10.1)), type(str(10.1)))

    # string function
    print('Capitalize :', o_str1.capitalize()) 
    print('endswith? : ', o_str2.endswith("s"))
    print('replace', o_str1.replace("Nice", "Good"))
    print('replace', o_str1.replace("th", "Good"))
    print('sorted', sorted(o_str1))
    print('Split : ', o_str4.split(" "))
    
    # sequence
    im_str = "Good boy!"
    print(dir(im_str))

    for i in im_str:
        print(i) 
    
    # slicing 
    print("slicing")
    str_s1 = "Nice Python"
    print(len(str_s1))
    print(str_s1[0])
    print(str_s1[0:3])
    print(str_s1[5:])
    print(str_s1[:len(str_s1)])
    print(str_s1[-1:])
    print(str_s1[1:4:2])

    print(str_s1[-1:])
    print(str_s1[1:-2])
    print(str_s1[::2])
    print(str_s1[::-1])
    
    # ascii 
    a = 'z'
    print(ord(a))
    print(chr(122))

