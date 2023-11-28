import time 
import threading 
import logging 
import concurrent.futures 
import random 
import queue

def producer(queue, event):
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info('Producer got message: %s', message)
        queue.put(message)
    logging.info('Producer received event Exiting') 


def consumer(queue, event):    
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info('Consumer storing message: %s (size=%d)', message, queue.qsize())
        
    logging.info('Producer received event Exiting') 


if __name__ == '__main__':
    format = '%(asctime)s %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.info('Main Thread : Before creating thread')

    pipeline = queue.Queue(maxsize=10)
    
    event = threading.Event() 
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
    
        time.sleep(0.1)
    
        logging.info('Main : about to set event')
    
        event.set()
        
        