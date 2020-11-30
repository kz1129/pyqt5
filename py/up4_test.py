import threading
import time

exitFlag = 0

class myThread ():
    def __init__(self, ID, name1, count):
        threading.Thread.__init__(self)
        self.ID = ID
        self.name1 = name1
        self.count = count
    def run(self):
        print ("开始线程：" + self.name1)
        print_time(self.name1, self.count, 5)
        print ("退出线程：" + self.name1)

def print_time(threadName, delay, count):
    while count:
        print(1)
        print(threadName)
        count = count - 1

x = myThread(1, 'ycy', 5)
x.run()