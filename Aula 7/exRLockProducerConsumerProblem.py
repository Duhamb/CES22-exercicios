import threading
import time
import random
from threading import Thread, Event
from queue import Queue

times = 10

class Box(object):
    lock = threading.RLock()
    def __init__(self):
        self.queue = Queue()
    def add(self, item):
        Box.lock.acquire()
        self.queue.put(item)
        Box.lock.release()
    def get(self):
        Box.lock.acquire()
        value = self.queue.get()
        Box.lock.release()
        return value
    def remove(self):
        Box.lock.acquire()
        self.queue.task_done()
        Box.lock.release()

class Producer(Thread):
    def __init__(self, box):
        Thread.__init__(self)
        self.box = box

    def run(self):
        for i in range(times):
            item = random.randint(0, 256)
            print('Producer notify: item N°{} added to box by {}\n'.format(item, self.name))
            box.add(item)
            time.sleep(1)

class Consumer(Thread):
    def __init__(self, box):
        Thread.__init__(self)
        self.box = box

    def run(self):
        while not box.queue.empty():
            item = box.get()
            print('Consumer notify: item N°{} removed from box by {}\n'.format(item, self.name))
            box.remove()
            time.sleep(1)

if __name__ == '__main__':
    box = Box()
    t1 = Producer(box)
    t2 = Consumer(box)
    t3 = Consumer(box)
    t4 = Consumer(box)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

