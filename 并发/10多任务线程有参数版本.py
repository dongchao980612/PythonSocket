import time
import threading      

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
    sing_thread = threading.Thread(target=sing, args=(3,))
    dance_thread = threading.Thread(target=dance, kwargs={'num': 3})
    sing_thread.start()
    dance_thread.start()
    sing_thread.join()
    dance_thread.join()
    endtime = time.time()
    print("总用时: {}".format(endtime - begintime))