"""
使用信号量实现进程共享队列

注意：
在Windows中，子进程使用全局变量获得的是其拷贝。
如果要使用全局变量，必须在main函数（父进程）中定义引用形式的局部变量，
并将其作为参数传入子进程——此时子进程拿到的是父进程中变量的引用，而非拷贝。
然后在多个子进程中用global声明的全局变量来保存传入的（实际上是同一份）参数，
以此达到共享全局变量的效果。
"""

from multiprocessing import Process, Semaphore, Lock, Queue
import time
from random import random

g_buffer = None
g_empty = None
g_full = None
g_lock = None

class Consumer(Process):
    def __init__(self, buffer, empty, full, lock):
        Process.__init__(self)
        self.buffer = buffer
        self.empty = empty
        self.full = full
        self.lock = lock

    def run(self):
        global g_buffer, g_empty, g_full, g_lock
        g_buffer = self.buffer
        g_empty = self.empty
        g_full = self.full
        g_lock = self.lock
        while True:
            g_full.acquire()
            g_lock.acquire()
            num = g_buffer.get()
            print(f'Consumer pop: {num}')
            time.sleep(1)
            g_lock.release()
            g_empty.release()


class Producer(Process):
    def __init__(self, buffer, empty, full, lock):
        Process.__init__(self)
        self.buffer = buffer
        self.empty = empty
        self.full = full
        self.lock = lock

    def run(self):
        global g_buffer, g_empty, g_full, g_lock
        g_buffer = self.buffer
        g_empty = self.empty
        g_full = self.full
        g_lock = self.lock
        while True:
            g_empty.acquire()
            g_lock.acquire()
            num = random()
            g_buffer.put(num)
            print(f'Producer append: {num}')
            time.sleep(1)
            g_lock.release()
            g_full.release()

if __name__ == '__main__':
    m_buffer = Queue(10)
    m_empty = Semaphore(2)
    m_full = Semaphore(0)
    m_lock = Lock()

    p = Producer(m_buffer, m_empty, m_full, m_lock)
    c = Consumer(m_buffer, m_empty, m_full, m_lock)
    p.daemon = True
    c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Main Process Ended')
