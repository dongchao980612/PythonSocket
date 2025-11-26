

import socket
import threading
from tkinter import Tk

def  recv_msg():
    while True:
        data_b = s.recv(1024)
        data_s = data_b.decode('utf-8')
        print("收到:", data_s)

if __name__ == '__main__':
    ip="120.0.0.1"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 9988))

    t = threading.Thread(target=recv_msg)
    t.start()

    root = Tk.Tk()
    root.title("聊天窗口")
    root.geometry("400x300")
    root.resizable(width=False, height=False)
    