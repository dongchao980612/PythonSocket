import threading
import time

def  work(num):
    for i in range(num):
        print("工作中...")
        time.sleep(1)

if __name__ == '__main__':
    begintime = time.time()
    # work_thread = threading.Thread(target=work, args=(3,), daemon=True)
    work_thread = threading.Thread(target=work, args=(3,))
    work_thread.daemon = True
    work_thread.start()
    time.sleep(2)
    endtime = time.time()
    print("主线程继续执行...")
    print("总用时: {}".format(endtime - begintime))