"""None"""

from multiprocessing import Process
import time

# def process(index):
#     "None"
#     print(f'Process: {index}')

class MyProcess(Process):
    """None"""
    def __init__(self, loop):
        "None"
        Process.__init__(self)
        self.loop = loop

    def run(self):
        "None"
        for count in range(self.loop):
            time.sleep(1)
            print(f'Pid: {self.pid} LoopCount: {count}')

if __name__ == '__main__':
    # for i in range(5):
    #     p = multiprocessing.Process(target=process, args=(i,))
    #     p.start()
    # print(f'CPU number: {multiprocessing.cpu_count()}')
    # for p in multiprocessing.active_children():
    #     print(f'Child process name: {p.name} id: {p.pid}')
    # print('Process Ended')
    processes = []
    for i in range(2, 5):
        p = MyProcess(i)
        processes.append(p)
        p.daemon = True
        p.start()
    for p in processes:
        p.join(1)
    print("Main Process Ended")
