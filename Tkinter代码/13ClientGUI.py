import tkinter as tk
from tkinter import scrolledtext, messagebox
import socket
import threading
import time

class SocketClientGUI:
    def __init__(self, win):
        self.win = win
        self.win.title("Socket聊天客户端")
        self.win.resizable(False, False)

        # 核心变量
        self.client_socket = None
        self.is_connected = False
        self.username = ""  # 存储当前客户端的用户名

        # ========== 1. 连接配置区域（新增用户名输入） ==========
        frame_config = tk.Frame(win)
        # 用户名输入行
        tk.Label(frame_config, text="用户名：", font=("微软雅黑", 11)).grid(row=0, column=0, padx=5, pady=5)
        self.entry_username = tk.Entry(frame_config, font=("微软雅黑", 11), width=15)
        self.entry_username.insert(0, f"用户{time.time()%1000:.0f}")  # 生成随机默认用户名
        self.entry_username.grid(row=0, column=1, padx=5)

        # IP/端口行
        tk.Label(frame_config, text="服务器IP：", font=("微软雅黑", 11)).grid(row=1, column=0, padx=5, pady=5)
        self.entry_ip = tk.Entry(frame_config, font=("微软雅黑", 11), width=15)
        self.entry_ip.insert(0, "127.0.0.1")
        self.entry_ip.grid(row=1, column=1, padx=5)

        tk.Label(frame_config, text="端口：", font=("微软雅黑", 11)).grid(row=1, column=2, padx=5)
        self.entry_port = tk.Entry(frame_config, font=("微软雅黑", 11), width=8)
        self.entry_port.insert(0, "8888")
        self.entry_port.grid(row=1, column=3, padx=5)

        # 连接/断开按钮
        self.btn_connect = tk.Button(frame_config, text="连接服务器", font=("微软雅黑", 11), 
                                    width=10, command=self.connect_server)
        self.btn_connect.grid(row=1, column=4, padx=10)
        self.btn_disconnect = tk.Button(frame_config, text="断开连接", font=("微软雅黑", 11), 
                                       width=10, command=self.disconnect_server, state=tk.DISABLED)
        self.btn_disconnect.grid(row=1, column=5, padx=10)
        frame_config.pack(fill=tk.X, padx=10)

        # ========== 2. 聊天记录区域 ==========
        frame_chat = tk.Frame(win)
        tk.Label(frame_chat, text="聊天记录：", font=("微软雅黑", 11)).pack(anchor=tk.W)
        self.text_chat = scrolledtext.ScrolledText(frame_chat, font=("微软雅黑", 10), 
                                                  width=65, height=30, state=tk.DISABLED)
        self.text_chat.pack(padx=5, pady=5)
        frame_chat.pack(fill=tk.BOTH, padx=10, pady=5)

        # ========== 3. 消息输入区域 ==========
        frame_input = tk.Frame(win, relief=tk.GROOVE, bd=1)
        tk.Label(frame_input, text="输入消息：", font=("微软雅黑", 11)).pack(side=tk.LEFT, padx=5, pady=5)
        self.entry_msg = tk.Entry(frame_input, font=("微软雅黑", 11), width=45)
        self.entry_msg.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
        self.entry_msg.bind("<Return>", lambda event: self.send_message())  # 回车发送
        
        self.btn_send = tk.Button(frame_input, text="发送", font=("微软雅黑", 11), 
                                 width=8, command=self.send_message, state=tk.DISABLED)
        self.btn_send.pack(side=tk.LEFT, padx=5, pady=5)
        frame_input.pack(fill=tk.X, padx=10, pady=10)

    def log_chat(self, msg):
        """添加聊天记录（线程安全）"""
        self.text_chat.config(state=tk.NORMAL)
        self.text_chat.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] {msg}\n")
        self.text_chat.see(tk.END)
        self.text_chat.config(state=tk.DISABLED)

    def connect_server(self):
        """连接服务器（先发送用户名）"""
        # 1. 获取并验证用户名
        self.username = self.entry_username.get().strip()
        if not self.username:
            messagebox.showwarning("提示", "用户名不能为空！")
            self.entry_username.focus()
            return
        
        # 2. 获取IP和端口
        try:
            ip = self.entry_ip.get().strip()
            port = int(self.entry_port.get().strip())
        except ValueError:
            messagebox.showerror("错误", "端口必须是数字！")
            return

        # 3. 创建socket并连接
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((ip, port))
        except Exception as e:
            messagebox.showerror("错误", f"连接失败：{str(e)}")
            return

        # 4. 发送用户名给服务器
        try:
            self.client_socket.send(self.username.encode("utf-8"))
        except Exception as e:
            messagebox.showerror("错误", f"发送用户名失败：{str(e)}")
            self.client_socket.close()
            return

        # 5. 更新状态
        self.is_connected = True
        self.btn_connect.config(state=tk.DISABLED)
        self.btn_disconnect.config(state=tk.NORMAL)
        self.btn_send.config(state=tk.NORMAL)
        self.entry_username.config(state=tk.DISABLED)  # 连接后禁止修改用户名
        self.entry_msg.focus()  # 光标定位到消息输入框

        # 6. 启动接收消息线程
        threading.Thread(target=self.receive_message, daemon=True).start()

    def disconnect_server(self):
        """断开连接"""
        self.is_connected = False
        if self.client_socket:
            try:
                self.client_socket.close()
            except:
                pass
        # 恢复状态
        self.btn_connect.config(state=tk.NORMAL)
        self.btn_disconnect.config(state=tk.DISABLED)
        self.btn_send.config(state=tk.DISABLED)
        self.entry_username.config(state=tk.NORMAL)  # 允许修改用户名
        self.log_chat("❌ 已断开与服务器的连接！")

    def receive_message(self):
        """接收服务器消息"""
        while self.is_connected:
            try:
                msg = self.client_socket.recv(1024).decode("utf-8")
                if not msg:
                    break
                self.log_chat(msg)
            except:
                break
        # 异常断开
        if self.is_connected:
            self.log_chat("❌ 与服务器的连接已异常断开！")
            self.disconnect_server()

    def send_message(self):
        """发送消息到服务器"""
        msg = self.entry_msg.get().strip()
        if not msg:
            messagebox.showwarning("提示", "📝 消息不能为空！请输入内容后发送")
            self.entry_msg.focus()
            return
        
        try:
            self.client_socket.send(msg.encode("utf-8"))
            self.log_chat(f"我：{msg}")
            self.entry_msg.delete(0, tk.END)
            self.entry_msg.focus()
        except Exception as e:
            messagebox.showerror("错误", f"发送失败：{str(e)}")
            self.disconnect_server()

if __name__ == "__main__":
    win = tk.Tk()
    app = SocketClientGUI(win)
    win.mainloop()