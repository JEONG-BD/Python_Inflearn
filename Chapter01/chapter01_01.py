

if __name__ == "__main__":
    # print Format 
    print("=====")

    x = 50 
    y = 100 
    text = 308276567
    n = 'Lee'

    ex1 = 'n = %s, s = %s, sum = %d' %(n , text, (x +y))
    print(ex1)
    
    ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=x+y)
    print(ex2)

    ex3 = f'n = {n}, s = {text}, sum = {x + y}'
    print(ex3)

    
    m = 100000000
    print(f'm : {m:,}')

    # ^ centr < left > right 
    t = 20
    print(f't {t:10}')
    print(f't {t:^10}')
    print(f't {t:<10}')
    print(f't {t:>10}')
    print(f't {t:-^10}')
    print(f't {t:*^10}')