import time
import multiprocessing  

def  sing(num):
    for i in range(num):
        print("唱歌中...")
        time.sleep(1)

def  dance(num):
    for i in range(num):
        print("跳舞中...")
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