"""使用Pool的map方法启动进程池

Pool.map(func, list)
将list的每个元素作为参数传给func，然后启动一个进程来执行func
"""

from multiprocessing import Pool
import urllib.request
import urllib.error

def scrape(url):
    try:
        urllib.request.urlopen(url)
        print(f'URL {url} Scraped~')
    except (urllib.error.HTTPError, urllib.error.URLError):
        print(f'URL {url} not Scraped!')

if __name__ == '__main__':
    pool = Pool(processes=3)
    urls = [
        'https://www.baidu.com',
        'http://www.meituan.com/',
        'http://blog.csdn.net/',
        'http://xxxyxxx.net'
    ]
    pool.map(scrape, urls)
    pool.close()
