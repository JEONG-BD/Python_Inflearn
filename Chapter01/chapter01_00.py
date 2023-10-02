

if __name__ == "__main__":
    print("Hello world!!")
    print("Python Start!!")
    print("P", "Y", "T", "H", "O", "N")
    print("P", "Y", "T", "H", "O", "N", sep="")
    print("test", "hanmail.net", sep="@")
    print("010", "2222", "3333", sep="-")

    # end option
    print("Welcome to", end=" ")
    print("IT News" )
    print("Web Site")
    
    # file option 
    import sys 
    print("Learn Python", file=sys.stdout)
    print()

    #format option (digit, string, float)
    print('%s %s' %('one', 'two'))
    print('{} {}'.format("one", "two"))
    print('{} {}'.format("one", 2))
    print('{1} {0}'.format("one", 2))
    
    #format s
    print('%10s' %('nice'))
    print('{:>10}'.format('nice'))
    print('%-10s' %('nice'))
    print('{:10}'.format('nice'))
    print('{:10}'.format('nice'))
    print('{:^10}'.format('nice'))
    print('%.5s'%('nice'))
    print('%.5s'%('pythonstudy'))
    print('{:10.5}'.format('pythonstudy'))

    #format d
    print('%d %d' %(1,2)) 
    print('{} {}'.format(1, 2))
    print('%4d' %(42))
    
    # format f 
    print('%f' % (3.145))
    print('%06.2f' %(3.141592))
    print('{:06.2f}'.format(3.141592))
