import timeit  
import asyncio
import threading 
from bs4 import BeautifulSoup
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor 


start = timeit.default_timer()

urls = ['http://daum.net', 
       'https://naver.com', 
       'http://mlbpark.donga.com', 
       'https://tistory.com', 
       'https://wemakeprice.com']


async def fetch(url, executor):
    print(f'Thread Name : {threading.current_thread().getName()} Start : {url}')
    res = await loop.run_in_executor(executor, urlopen, url)
    
    return res.read()[0:5]



async def main():
    # Non block
    executor = ThreadPoolExecutor(max_workers=10)

    futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]

    rst = await asyncio.gather(*futures)
    print(f'Result : {rst}')

if __name__ == '__main__' : 
    print('asyncio')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    duration = timeit.default_timer() - start 

    print(f'Total Running Time : {duration}')

