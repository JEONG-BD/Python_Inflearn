import os 
import time 
from concurrent.futures import ThreadPoolExecutor, wait, as_completed


WORK_LIST = [10000, 100000, 1000000, 10000000]
futures_list = []

def sum_generator(n):
    sum_1 = sum(i for i in range(1, n+1))
    print(sum_1)

def main():
    start_time = time.time()
    worker = min(10, len(WORK_LIST))

    with ThreadPoolExecutor() as executor : 
        for work in WORK_LIST:
            print(work)
            futures = executor.submit(sum_generator, work)
            futures_list.append(futures)
            print('Scheduled for {} : {}'.format(work, futures))
            print()
        # result = wait(futures_list, timeout = 7)
        # print('Cimpleted Tasks : '+ str(result.done) )
        # print('Pending ones after waiting for 7 seconds ' + str(result.not_done))

        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled
            print('Future Result : {} :  Done {}'.format(result, done))
            print('Future cancelled : {} '.format(cancelled))
            

    end_time = time.time() - start_time

    msg = '\nResult -> {} Time : {:.2f}s'

    #print(msg.format(list(result), end_time))
    print(end_time)
    print('')
if __name__ == '__main__':
    main()
