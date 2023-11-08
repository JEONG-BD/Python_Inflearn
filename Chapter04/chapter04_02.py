import logging
import time 
import threading 



def thread_func(name, d):
    logging.info(f"Sub Thread {name} starting")
    time.sleep(3)
    for i in d :
        logging.info(f"Sub Thread {name} : {i}")
    logging.info(f"Sub Thread {name} finishing")
   
if __name__ == '__main__':
    print('Thread')
    format = '%(asctime)s : %(message)s'
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt='%H:%M:%S')
    logging.info('Main Thread : before creating thread')
    x = threading.Thread(target=thread_func, args=('First', range(20)), daemon=True)
    y = threading.Thread(target=thread_func, args=('Second', range(10)), daemon=True)

    logging.info('Main Thread : before running thread')
    print(x.isDaemon())
    print(y.isDaemon())
    x.start()
    y.start()
    #x.join()
    #y.join()

    logging.info('Main Thread : wait for the thread to finish')
    logging.info('Main Thread : all done')
