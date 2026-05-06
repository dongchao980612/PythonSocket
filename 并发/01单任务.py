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
    sing()
    dance()
    endtime = time.time()
    print(f"总用时: {endtime - begintime}")