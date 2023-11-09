import time 
import logging 
import threading

from concurrent.futures import ThreadPoolExecutor

def task(name):
    logging.info(f'Sub Thread : {name} starting ')
    result = 0 

    for i in range(101):
        print(f'{name} {i}')
        result += i

    
    logging.info(f'Sub Thread {name} finishing result {result}')
    return result
     
def main():
    format = '%(asctime)s %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.info('Main Thread : before creating thread')

    #excutor = ThreadPoolExecutor(max_workers=3)

    #task1 = excutor.submit(task, ('First'))
    #task2 = excutor.submit(task, ('Second'))
    #print(task1.result())
    #print(task2.result())
    
    with ThreadPoolExecutor(max_workers=3) as executor : 
        tasks = executor.map(task, ['First', 'Second'])

        print(list(tasks))

if __name__ == '__main__': 
    main()
    

  


