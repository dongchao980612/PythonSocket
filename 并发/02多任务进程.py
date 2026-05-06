import time
import multiprocessing  

def  sing():
    for i in range(3):
        print("唱歌中...")
        time.sleep(1)

def  dance():
    for i in range(3):
        print("跳舞中...")
        time.sleep(1)

if __name__ == '__main__':
    begintime = time.time()
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)
    sing_process.start()
    dance_process.start()
    sing_process.join()
    dance_process.join()
    endtime = time.time()
    print("总用时: {}".format(endtime - begintime))