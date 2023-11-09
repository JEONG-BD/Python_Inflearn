import logging 
import time 
import threading
from concurrent.futures import ThreadPoolExecutor 

class FaskDataStore(object):

    def __init__(self):
        self.value = 0 
        self._lock = threading.Lock()


    def update(self, n):
        logging.info(f'Thread {n} starting update')
        
        # self._lock.acquire()
        # logging.info(f'Thread {n} has lock')
        # 
        # local_copy = self.value 
        # local_copy += 1 
        # time.sleep(0.1)
        # self.value = local_copy 
# 
        # logging.info(f'Thread {n} release lock')
        # 
        # self._lock.release()
        
        with self._lock:
            logging.info(f'Thread {n} has lock')
        
            local_copy = self.value 
            local_copy += 1 
            time.sleep(0.1)
            self.value = local_copy 

            logging.info(f'Thread {n} release lock')
    
        logging.info(f'Thread {n} finishing update')

if __name__ == '__main__':
    format = '%(asctime)s %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

    logging.info('Main Thread : Before creating thread')

    store = FaskDataStore()
    logging.info(f'Main Thread : Starting value is {store.value}')

    with ThreadPoolExecutor(max_workers=4) as executor:
        for n in ['First', 'Second', 'Third']:
            executor.submit(store.update, n)

    logging.info(f'Main Thread : Ending value is {store.value}')

