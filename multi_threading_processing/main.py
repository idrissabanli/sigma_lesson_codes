import time
import threading
import multiprocessing

def do_something():
    print('proccess started')
    time.sleep(1)
    print('proccess done')

t1 = time.time()
threads = []

for i in range(1000):
    thread = threading.Thread(target=do_something)
    thread.start()
    threads.append(thread)

for i in threads:
    i.join()

t2 = time.time()

dt = t2-t1
print(dt)
