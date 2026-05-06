import threading
import time


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
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)
    sing_thread.start()
    dance_thread.start()
    sing_thread.join()
    dance_thread.join()
    endtime = time.time()
    print("总用时: {}".format(endtime - begintime))
    # 总用时: 3.119548797607422
