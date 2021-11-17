"""通过管道实现进程间通信"""

from multiprocessing import Process, Pipe

class Consumer(Process):
    def __init__(self, pipe):
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        self.pipe.send('Consumer Words')
        print(f'Consumer Received: {self.pipe.recv()}')

class Producer(Process):
    def __init__(self, pipe):
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        print(f'Producer Received: {self.pipe.recv()}')
        self.pipe.send('Producer Words')

if __name__ == '__main__':
    my_pipe = Pipe()
    p = Producer(my_pipe[0])
    c = Consumer(my_pipe[1])
    p.daemon = True
    p.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Main Process Ended')
