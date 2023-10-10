

if __name__ == "__main__":
    # if 
    if True : 
        print('Good')
    
    if False :
        print("Bad")

    if False :
        print("Hot")
    else :
        print("Cool")
    
    x = 15 
    y = 10 

    print(x == y)
    print(x != y)
    print(x > y)
    print(x < y)

    city = "Seoul"

    if city :
        print("You are in", city)
    else :
        print("Please enter your city")
    

    city2 = ""

    if city2 :
        print("You are in", city)
    else :
        print("Please enter your city")
    

    #and or not 

    a = 75 
    b = 40 
    c = 10 
    print('and', a > b and b > c )
    print('or', a > b or b > c)
    print('not', not a > b)
    print('not', not b > c)

    print('e1', 3 + 10 > 7 + 3)
    print('e2', 5 + 10 * 3 > 7 + 3 * 20)
    print('e3', 5 + 10 > 3 and 7 + 3 == 10)

    score1 = 90 
    score2 = 'A'

    if score1 >= 90 and score2 == 'A':
        print("Pass")
    else :
        print("Fail")

    id1 = 'VIP'
    id2 = 'ADMIN'
    grade = 'PLATINUM'

    if id1 == 'VIP' and id2 == 'ADMIN':
        print('ADMIN')

    if id1 == 'VIP' and grade == 'PLATINUM':
        print("ROOT")

    num = 90 

    if num >= 90:
        print('Grade A')
    elif num >= 80:
        print('Grade B')
    elif num >= 70:
        print('Grade C')
    else :
        print('Grade D') 

    grade = 'A'
    total = 80 

    if grade == 'A':
        if total >= 90 :
            print('100%')
        elif total >= 80 :
            print('80%')
        else : 
            print('None')
    else :
        print('Fail')

    
    # in not in 

    q = [10, 20, 30]
    w = {70, 80, 90, 100}
    e = {'name':'lee', 'city':'seoul', 'grade':'A'}
    r = (10, 12 , 14)

    print(15 in q)
    print(90 in w)
    print('seoul'in e.values())