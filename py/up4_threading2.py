import threading
import time

class kzaThread(threading.Thread):
    def __init__(self, id, name, counter, delay):
        threading.Thread.__init__(self)
        #虽然没有定义这些参数，后面的self会自动为这个类生成参数
        self.id = id
        self.name = name
        self.counter = counter
        self.delay = delay
    #重写父类的run方法
    def run (self):
        # 获取锁，用于线程同步
        threadLock.acquire()
        print('开始线程', self.name)
        print_time(self.name, self.counter, self.delay)
        # 释放锁
        print('结束线程', self.name)
        threadLock.release()
        
def print_time (name, counter, delay):
    while counter:
        print( name ,'正在运行，时间：',time.ctime(time.time()))
        time.sleep(delay)
        counter -= 1


threadLock = threading.Lock()
threads = []

thread1 = kzaThread(1, '李智颖在玩游戏', 5, 2)
thread2 = kzaThread(2, '李智颖在看电视剧', 8, 1)
thread3 = kzaThread(3, '李智颖在吹逼', 10, 3)

thread1.start()
thread2.start()
thread3.start()
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

# 等待所有线程完成
for t in threads:
    t.join()
print('退出主程序')