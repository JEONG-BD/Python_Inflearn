
if __name__ == "__main__":
    print("variable ")

    n = 700 
    print(f"{n * 700}")
    print(f"type : {type(n)}")
    
    x = y = z = 700 
    print(f"{x} {y} {z}")

    var = 75 
    var = "Change Value"
    print(var)
    print(type(var))

    # Object Reference
    print(300)
    print(int(300))

    n = 777
    print(n, type(n))

    m = n 
    print(m, n)
    m = 400 
    print(m, n)

    # Identity 
    m = 800 
    n = 600 
    print(id(m))
    print(id(n))
    print(id(m) == id(n))

    m = 800 
    n = 800 
    print()
    print(id(m) == id(n))

    # naming 
    # Camel Case : numberOfCollegeGraduates 
    # Pascal Case : NumberOfCollegeGradutes 
    # Snake Case : number_of_college_gradutes 

    age = 1
    Age = 1 
    AGE = 1 
    a_g_e = 1 
    _age = 1 
    age_ = 1 

    #reserved word 
    # for = 3 
    # as = 3 
     
    