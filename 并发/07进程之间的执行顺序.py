import multiprocessing

import os
import time

def  work():
    cur_thread = os.getpid()
    time.sleep(5)
    print(f"当前进程: {cur_thread}")

if __name__ == '__main__':
    for i  in range(10):
        t = multiprocessing.Process(target=work)
        t.start()
  