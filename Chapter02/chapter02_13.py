from typing import Union, Optional 



b = 20 
c = 30
def func_v1(a : Union[str, int]): 
    """
    NAME : Function func_v1
    CREATE USER : Admin
    UPDATE USER : Admin
    CREATE DATE : 2023.10.21
    UPDATE DATE : 2023.10.21 
    """
    global c 
    print(a, type(a))
    print(b) 
    print(c)
    c = 40 
    print(c)

class Averager():
    """
    NAME : Class Averager 
    CREATE USER : Admin
    UPDATE USER : Admin
    CREATE DATE : 2023.10.21
    UPDATE DATE : 2023.10.21 
    """
    def __init__(self):
        self._series = []
    
    def __call__(self, v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series) 
    
if __name__ == "__main__":
    func_v1(10)

    # closure 
    a = 100 
    print(a + 100) 
    print(a + 1000)
    print(sum(range(1, 51)))
    print(sum(range(51, 101)))

    avg_cls = Averager()
    print(avg_cls(10))
    print(avg_cls(30))
    print(avg_cls(50))