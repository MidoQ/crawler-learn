"""给进程加锁实现互斥"""

from multiprocessing import Process, Lock
import time

class MyProcess(Process):
    "None"
    def __init__(self, loop, lock):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            self.lock.acquire()
            print(f'Pid: {self.pid} LoopCount: {count}')
            self.lock.release()

if __name__ == "__main__":
    my_lock = Lock()
    for i in range(10, 15):
        p = MyProcess(i, my_lock)
        p.start()
