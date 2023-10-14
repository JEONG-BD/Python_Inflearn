import traceback 

if __name__ == "__main__":
    print("exception")
    name = ["Kim", "Lee", "Park"]
    try : 
        z = "Kim"
        x = name.index(z)

        print("{} Found it ! {} in name".format(z, x + 1))
    except ValueError as ex : 
        print("Not found it! - Occurred ValueError")

    except Exception as ex :
        print(traceback.format_exc())
    else :
        print("OK!")


    try : 
        a = "Park1"
        if a == "Park":
            print("OK Pass")
        else :
            print("Fail")    
            raise ValueError
    except ValueError :
        print("Occured! Exception!")