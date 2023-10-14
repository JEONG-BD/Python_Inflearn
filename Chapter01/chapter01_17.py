import Chapter01_sub.sub1.module1
import Chapter01_sub.sub2.module2


from Chapter01_sub.sub1 import module1 as m1 
from Chapter01_sub.sub2 import module2 as m2

if __name__ == "__main__":
    print("package")
    Chapter01_sub.sub1.module1.mod1_test1()
    Chapter01_sub.sub1.module1.mod1_test2()
    Chapter01_sub.sub2.module2.mod2_test1()
    Chapter01_sub.sub2.module2.mod2_test2()