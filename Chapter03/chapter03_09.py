import datetime


class ParentEx1():

    def __init__(self):
        self.value = 5 
    
    def get_value(self):
        return self.value
    
class ChildEx1(ParentEx1):
    pass 

class PareneEx2():

    def __init__(self):
        self.value = 5 
    
    def get_value(self):
        return self.value

class ChildEx2(PareneEx2):
    def get_value(self):
        return self.value * 10

class Logger(object):
    def log(self, msg):
        print(msg)

class TimeStampLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(ts=datetime.datetime.now(), msg=msg)
        super(TimeStampLogger, self).log(message)

class DateStampLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(ts=datetime.datetime.now().strftime('%Y-%m-%d'), msg=msg)
        super(DateStampLogger, self).log(message)


if __name__ == '__main__':
    print('method overriding')

    p1 = ParentEx1()
    c1 = ChildEx1() 

    print(f'Ex01 {c1.get_value()}')
    print(f'Ex01 {dir(c1)}')
    #print(f'Ex01 {dir(ParentEx1)}')
    #print(f'Ex01 {dir(ChildEx1)}')
    print(f'Ex01 {ParentEx1.__dict__}')
    print(f'Ex01 {ChildEx1.__dict__}')
    print()
    c2 = ChildEx2()
    print(f'Ex02 {c2.get_value()}')

    l = Logger()
    t = TimeStampLogger()
    d = DateStampLogger()

    print(l.log('test'))
    print(t.log('test'))
    print(d.log('test'))

