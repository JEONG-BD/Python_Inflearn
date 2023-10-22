from collections import abc 

class WordSplitGenerator :
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word 
        return  
    
    def __repr__(self):
        return 'WordSplitGenerator (%s)' %(self._text) 

class WordSplit:
    """
    NAME : Class WordSplit
    CREATE USER : Admin
    UPDATE USER : Admin
    CREATE DATE : 2023.10.22 
    UPDATE DATE : 2023.10.22
    DESCRIPTION : 
    """
    def __init__ (self, text):
        self._idx = 0 
        self._text = text.split(' ')

    def __next__(self) : 
        print('Called __next__')
        try :
            word = self._text[self._idx]
            print(word)
        except IndexError : 
            raise StopIteration('Stopped Iteration')
        
        self._idx += 1 
        return word
    
    def __repr__(self):
        return 'WordSplit(%s)' %(self._text)

def number_generator():
    yield 0 
    yield 1 
    yield 2 

def one_generator():
    yield 1 
    return 'return value'






if __name__ == '__main__':
    print('concurrency')
    
    t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(dir(t))

    for c in t:
        print(c)
    print()
    w = iter(t)
    # print(w)
    print(next(w))
    print(next(w))

    while True :
        try:
            print(next(w))
        except StopIteration : 
            break
    
    print(hasattr(t, '__iter__'))
    print(isinstance(t, abc.Iterable))


    wi = WordSplit('Do today what you could to tommorrow')
    print(wi)
    print(next(wi))
    print(next(wi))
    print(next(wi))
    print(next(wi))
    print(next(wi))
    print(next(wi))

    wi2 = WordSplitGenerator('Do today what you could to tomorrow')
    
    wt = iter(wi2)
    print(wt, wi2)
    print(next(wt))


    for i in number_generator():
        print(i)
    
    g = number_generator()
    print(g)
    print(dir(g))
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())

    try : 
        g = one_generator()
        print(next(g))
        print(next(g))
    except StopIteration as ex:
        print(ex)