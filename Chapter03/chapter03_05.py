import time 


class ExecutorTime(object):

    def __init__(self, msg):
        self._msg = msg 
    
    def __enter__(self): 
        self._start = time.monotonic()
        return self._start 

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type : 
            print('Logging exception {}'.format(exc_type, exc_value, exc_traceback))
        else :
            print('{} {}'.format(self._msg, time.monotonic() - self._start)) 
        return True 

if __name__ == '__main__':
    # Ex01 
    
    with ExecutorTime('Start Task!') as v :
        print('Received start monotonic1 : {}'.format(v))
        for i in range(100000):
            pass
        raise Exception('Raise Exception!') 