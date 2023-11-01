import os 
import sys 
import logging 

logging.basicConfig(
    format='%(asctime)s %(message)s', 
    level = logging.INFO, 
    datefmt='%Y-%m-%d %H:%M:%S'
)

class LoggedScoreAccess(object):

    def __init__(self, value=50):
        self.value = value 
    
    def __get__(self, obj, objtype=None):
        logging.info('Accessing %r giving %r' ,'score', self.value)
        return self.value 

    def __set__(self, obj, value):
        logging.info('Accessing %r giving %r' ,'score', self.value)
        self.value = value  

class Student(object):

    score = LoggedScoreAccess()

    def __init__(self, name):
        self.name = name 

class DirectoryFileCount():
    
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class DirectoryPath:
    size = DirectoryFileCount()

    def __init__(self, dirname):
        self.dirname = dirname 

if __name__ == '__main__':
    print(os.getcwd())
    s = DirectoryPath('./Chapter03')
    print(dir(s))
    print(s.dirname)
    print(s.__dict__)
    print(s.size)
    print("*"*6)

    s1 = Student('Kim')
    s2 = Student('Lee')

    print(s1.score)
    print(s2.score)

    s1.score +=20 
    print(s1.score)

    print(vars(s1))
    print(vars(s2))