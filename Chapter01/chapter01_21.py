import pickle 
import os 

if __name__ == "__main__":
    print("file")
    # read 
    # with open("./Chapter01_resource/it_news.txt", "rt", encoding="UTF-8") as f:
    #     print(type(f))

    f = open("./Chapter01/Chapter01_resource/it_news.txt", "rt", encoding="UTF-8") 
    print(type(f))
    print(f.encoding)
    print(f.name)
    print(f.mode)
    cts = f.read()
    print(cts)
    f.close()

    with open("./Chapter01/Chapter01_resource/it_news.txt", "rt", encoding="UTF-8")  as f :
        #c = f.read()
        #print(c)
        #print(list(c))
        #print(iter(c))
        #c = f.read(20)
        #print(c)
        cts = f.readlines()
        print(cts)

        for c in cts :
            print(c)
    print(os.getcwd())
    with open("./Chapter01/Chapter01_resource/test1_01.txt", 'w') as f :
         f.write("test1_01\n")
        
    with open("./Chapter01/Chapter01_resource/test1_01.txt", 'at') as f :
         f.write("test1_02\n")

    with open("./Chapter01/Chapter01_resource/test1_02.txt", 'at') as f :
         lst = ["Orange", "Apple", "Banana", "Melon"]
         result = list(map(lambda x : x +"\n", lst))
         f.writelines(result)
    
    with open("./Chapter01/Chapter01_resource/test1_03.txt", "w") as f : 
         print("Test text write!", file=f)
         print("Test text write!", file=f)
         print("Test text write!", file=f)

    