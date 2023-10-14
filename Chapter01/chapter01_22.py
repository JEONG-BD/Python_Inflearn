import os 
import sys 
import csv 

if __name__ == "__main__":
    with open("./Chapter01/Chapter01_resource/test1.csv", "r") as f :
        reader = csv.reader(f)
        next(reader)
        print(type(reader))
        print(dir(reader))

        for c in reader:
            print(c)
            print(''.join(c))

    with open("./Chapter01/Chapter01_resource/test2.csv", "r") as f :
        reader = csv.reader(f, delimiter="|")

        for c in reader:
            print(c)

    with open("./Chapter01/Chapter01_resource/test2.csv", "r") as f :
        reader = csv.DictReader(f, delimiter="|")
        print(type(reader))
        print(dir(reader))
        for c in reader:
            print(c)

    w = [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9], 
         [10, 11, 12], 
         [13, 14, 15], 
         [16, 17, 18], 
         [19, 20, 33]]
    
    with open("./Chapter01/Chapter01_resource/test1_01.csv", "w", encoding="UTF-8") as f :
        print(dir(f))
        wt = csv.writer(f)

        for v in w :
            wt.writerow(v)
    

    with open("./Chapter01/Chapter01_resource/test1_02.csv", "w", encoding="UTF-8") as f :
        
        fields = ["One", "Two", "Three"]

        wt = csv.DictWriter(f, fieldnames=fields)
        wt.writeheader()

        for v in w:
            wt.writerow({"One":v[0], "Two":v[1], "Three":v[2]})