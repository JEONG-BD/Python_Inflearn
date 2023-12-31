import logging 
import threading
import time 

def thread_func(name):
    logging.info(f"Sub Thread {name} starting")
    time.sleep(3)
    logging.info(f"Sub Thread {name} finishing")
    


if __name__ == '__main__':
    print("Thread")
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main Thread:before creating thread")

    x = threading.Thread(target=thread_func, args=('First', ))
    logging.info("Main Thread:before running thread")

    x.start()
    x.join()

    logging.info("Main Thread:wait for the thread to finish")
    logging.info("Main Thread:all done")
