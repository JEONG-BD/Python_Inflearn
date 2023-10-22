import os 
import time 

from concurrent import futures 

WORK_LIST = [10000, 100000, 1000000, 10000000]

def sum_generator(n):
    return sum(n for n in range(1, n+1))


def main(): 
    worker = min(10, len(WORK_LIST))

    start_tm = time.time()

    with futures.ProcessPoolExecutor() as executor : 
        result = executor.map(sum_generator, WORK_LIST)

    end_tm = time.time() - start_tm 

    msg = '\nResult -> {} Time : {:.2f}s'

    print(msg.format(list(result), end_tm))

if __name__ == '__main__':
    main()



