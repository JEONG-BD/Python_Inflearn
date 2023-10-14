import sys 
import pickle
import os 
import random 
import time 
import webbrowser 

if __name__ == "__main__":
    print(sys.argv)
    print(sys.path)

    # f = open("test.obj", "wb") 
    # obj = {1:"python", 2:"study", 3:"basic"}
    # pickle.dump(obj, f)
    # f.close 
    # with open("test.obj", "wb") as f :
    #     obj = {1:"python", 2:"study", 3:"basic"}
    #     pickle.dump(obj, f)
    print(os.environ)
    print(os.getcwd())
    print(time.time())
    print(time.localtime(time.time()))
    print(time.ctime())

    print(time.strftime("%Y %m %D %H:%M:%S", time.localtime(time.time())))

    for i in range(5):
        print(i)
        # time.sleep(2)

    print(random.random())
    print(random.randint(1, 45))
    print(random.randrange(1, 45))
    d = [1, 2, 3, 4, 5]
    random.shuffle(d)
    print(d)
    e= random.choice(d)
    print(e)

    webbrowser.open("http://google.com")