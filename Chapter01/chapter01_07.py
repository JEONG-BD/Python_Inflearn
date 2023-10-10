

if __name__ == "__main__":
    # dictionary
    dic_a = {'name':'Kim', 'phone':'01033337777', 'birth':'870514'}
    dic_b = {0:'Hello Python'}
    dic_c = {'arr ': [1, 2, 3, 4]}
    dic_d = {
        'Name':'NiceMan', 
        'City':'Seoul', 
        'Grade':'A', 
        'Status':True}
    
    dic_e = dict([
        ('Name' , 'NiceMan'),
        ('City' , 'Seoul'), 
        ('Grade', 'A')
    ])
    
    dic_f = dict(Name = 'NiceMan', City='Seoul', Grade='A')
    print(type(dic_a), dic_a) 
    print(type(dic_b), dic_b)
    print(type(dic_c), dic_c)
    print(type(dic_d), dic_d)
    print(type(dic_e), dic_e)
    print(type(dic_f), dic_f)

    # key 
    print(dic_a["name"])
    print(dic_a.get('name'))
    print(dic_a.get('Name'))
    print(dic_b[0])
    print(dic_f.get('City'))
    print(dic_a)
    dic_a['address'] = 'Buan'
    print(dic_a)

    dic_a['rank'] = [1, 2, 3]
    print(dic_a)
    print(len(dic_a))

    for i in dic_a:
        print(i)
    
    # keys 
    print(dir(dic_a))
    print(dic_a.keys())
    print(type(dic_a.keys()))
    print(list(dic_a.keys()))

    # values 
    print(dic_a.values())
    print(list(dic_a.values()))
    print(dic_a.items())

    print(dic_a.pop('name'))
    print(dic_a)

    print(dic_f.popitem())
    print(dic_f.popitem())
    print(dic_f.popitem())
    print(dic_f)

    print('birth' in dic_a)

    dic_a.update(birth='910904')
    print(dic_a)

    

    