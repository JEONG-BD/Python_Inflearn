import contextlib 
import time 


@contextlib.contextmanager
def my_file_writer(file_name, method):
    f = open(file_name, method)
    yield f # __enter__ 
    f.close() # __exit__ 

@contextlib.contextmanager
def my_time_record(msg):
    start = time.monotonic()
    try :
        yield start 
    except BaseException as e :
        print('Logging exception {} {}'.format(msg, e))
        raise
    else :
        print('{} {}'.format(msg, time.monotonic() - start))
    

if __name__ == '__main__':

    with my_file_writer('./Chapter03/Chapter03_resource/testfile03.txt', 'w') as f :
        f.write('Context Manager Test3\n Context Library Test3')
    
    with my_time_record('Start job') as v : 
        print('Received start monotonic2 {}'.format(v))
        for i in range(10000000):
            pass 
        raise ValueError('occurred')
