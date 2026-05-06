import threading
import time


def work():
    cur_thread = threading.current_thread()
    time.sleep(1)
    print("当前线程ID: {}".format(cur_thread.ident))


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=work)
        t.start()
