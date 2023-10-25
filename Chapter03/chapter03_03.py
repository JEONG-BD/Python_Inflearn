import copy 

if __name__ == '__main__':
    # shallow, deep copy
     
    # Ex01 Copy 
    list_a = [1, 2, 3, 
              [4, 5, 6], 
              [7, 8, 9]]
    
    list_b = list_a 
    print(id(list_b), id(list_a))
    
    list_b[2] = 100 
    print(id(list_b), id(list_a))
    print(list_b, list_a)    

    list_b[3][2] = 200 
    print(id(list_b), id(list_a))
    print(list_b, list_a)    

    # Ex02 Shallow Copy 
    c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
    d_list = copy.copy(c_list)
    print(id(c_list), id(d_list))
    d_list[1] = 100 
    print(c_list, d_list)
    d_list[3].append(1000)
    d_list[4][1] = 2000
    print(c_list, d_list)
    

    # Ex03 Deep Copy 
    e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
    f_list = copy.deepcopy(e_list)

    print(id(e_list), id(f_list))
    e_list[1] = 100 
    print(e_list, f_list)
    e_list[3].append(1000)
    f_list[4][1] = 2000
    print(e_list, f_list)
    