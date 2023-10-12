

if __name__ == "__main__":
    print('input')
    #name = input("Enter your name")
    #grade = input("Enter your grade")
    #company = input("Enter your company")
    #print(name)
    #print(grade)
    #print(company) 
    #num = input("Enter your number")
    #print(num, type(num))
    #first_num = int(input("Enter first number")) 
    #second_num = int(input("Enter secodde number"))
    #print(first_num + second_num)

    #print("First Name {0} Last Name {1}".format(input("Enter your First name"), input("Enter your Last name")))
    # try :
    #     n = int(input("Enter your favorite number : "))
    #     print(f"OK your number is {n}")
    # except ValueError as ex: 
    #     print(f"This is not o number")
    while True :
        try :
            n = int(input("Enter your number"))
            print(f"your number {n}")
            break
        except ValueError :
            print("This not a number")