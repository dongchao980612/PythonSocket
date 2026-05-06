import multiprocessing
import time

def  work(num):
    for i in range(num):
        print("工作中...")
        time.sleep(1)

if __name__ == '__main__':
    begintime = time.time()
    work_process = multiprocessing.Process(target=work, args=(4,))
    work_process.start()
    time.sleep(2)
    endtime = time.time()
    print("主进程继续执行...")
    print("总用时: {}".format(endtime - begintime))