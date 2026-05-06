import multiprocessing
import os
import time


def sing(num):
    print("唱歌进程ID: {}".format(os.getpid()))
    print("父进程ID: {}".format(os.getppid()))
    for i in range(num):
        # print("唱歌中...")
        time.sleep(1)


def dance(num):
    print("跳舞进程ID: {}".format(os.getpid()))
    print("父进程ID: {}".format(os.getppid()))
    for i in range(num):
        # print("跳舞中...")
        time.sleep(1)


if __name__ == '__main__':
    begintime = time.time()
    sing_process = multiprocessing.Process(target=sing, args=(3,))
    dance_process = multiprocessing.Process(target=dance, kwargs={'num': 3})
    sing_process.start()
    dance_process.start()
    sing_process.join()
    dance_process.join()
    endtime = time.time()
    print("总用时: {}".format(endtime - begintime))
    print("主进程ID: {}".format(os.getpid()))
