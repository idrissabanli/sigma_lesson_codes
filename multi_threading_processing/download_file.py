import time
import threading
import multiprocessing
import requests
import concurrent 

def download_image(index):
    print('proccess started')
    res = requests.get('https://picsum.photos/200/300')
    with open(f'downloads/image_{index}.png', 'wb') as f:
        f.write(res.content)
    print('proccess done')

if __name__ == "__main__":
    t1 = time.time()
    threads = []

    for i in range(50):
        t = multiprocessing.Process(target=download_image, args=(1,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    t2 = time.time()

    dt = t2-t1
    print(dt)
