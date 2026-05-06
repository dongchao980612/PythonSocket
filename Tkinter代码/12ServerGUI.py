import tkinter as tk
from tkinter import scrolledtext, messagebox
import socket
import threading
import time

class SocketServerGUI:
    def __init__(self, win):
        self.win = win
        self.win.title("Socket聊天服务器")
        # self.win.geometry("600x500")
        self.win.resizable(False, False)

        # 核心变量：修改clients为字典 {client_socket: (addr, username)}
        self.server_socket = None
        self.is_running = False
        self.clients = {}  # 键：客户端socket，值：(地址, 用户名)
        self.clients_lock = threading.Lock()

        # ========== 1. 地址端口输入区域 ==========
        frame_addr = tk.Frame(win)
        tk.Label(frame_addr, text="服务器IP：", font=("微软雅黑", 11)).grid(row=0, column=0, padx=5, pady=10)
        self.entry_ip = tk.Entry(frame_addr, font=("微软雅黑", 11), width=15)
        self.entry_ip.insert(0, "127.0.0.1")
        self.entry_ip.grid(row=0, column=1, padx=5)

        tk.Label(frame_addr, text="端口：", font=("微软雅黑", 11)).grid(row=0, column=2, padx=5)
        self.entry_port = tk.Entry(frame_addr, font=("微软雅黑", 11), width=8)
        self.entry_port.insert(0, "8888")
        self.entry_port.grid(row=0, column=3, padx=5)

        self.btn_start = tk.Button(frame_addr, text="启动服务", font=("微软雅黑", 11), 
                                  width=10, command=self.start_server)
        self.btn_start.grid(row=0, column=4, padx=10)
        self.btn_stop = tk.Button(frame_addr, text="停止服务", font=("微软雅黑", 11), 
                                 width=10, command=self.stop_server, state=tk.DISABLED)
        self.btn_stop.grid(row=0, column=5, padx=10)
        frame_addr.pack(fill=tk.X, padx=10)

        # ========== 2. 在线人数+在线用户显示 ==========
        frame_count = tk.Frame(win)
        tk.Label(frame_count, text="当前在线人数：", font=("微软雅黑", 11)).grid(row=0, column=0, padx=5, pady=5)
        self.label_count = tk.Label(frame_count, text="0", font=("微软雅黑", 11, "bold"), fg="red")
        self.label_count.grid(row=0, column=1, padx=5)
        
        # 新增：显示在线用户名
        tk.Label(frame_count, text="在线用户：", font=("微软雅黑", 11)).grid(row=0, column=2, padx=5, pady=5)
        self.label_users = tk.Label(frame_count, text="无", font=("微软雅黑", 11), fg="#0066cc")
        self.label_users.grid(row=0, column=3, padx=5)
        frame_count.pack(fill=tk.X, padx=10)

        # ========== 3. 日志显示区域 ==========
        frame_log = tk.Frame(win)
        tk.Label(frame_log, text="服务器日志：", font=("微软雅黑", 11)).pack(anchor=tk.W)
        self.text_log = scrolledtext.ScrolledText(frame_log, font=("微软雅黑", 10), 
                                                 width=70, height=25, state=tk.DISABLED)
        self.text_log.pack(padx=5, pady=5)
        frame_log.pack(fill=tk.BOTH, padx=10, pady=5)

    def log(self, msg):
        """向日志区域添加消息（线程安全）"""
        self.text_log.config(state=tk.NORMAL)
        self.text_log.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] {msg}\n")
        self.text_log.see(tk.END)
        self.text_log.config(state=tk.DISABLED)

    def update_online_info(self):
        """更新在线人数和在线用户名（线程安全）"""
        with self.clients_lock:
            count = len(self.clients)
            # 提取所有用户名，用逗号分隔
            usernames = [v[1] for v in self.clients.values()] if count > 0 else ["无"]
            username_str = ", ".join(usernames)
        
        self.label_count.config(text=str(count))
        self.label_users.config(text=username_str)
        self.log(f"在线状态更新：人数={count}，用户={username_str}")

    def start_server(self):
        """启动服务器"""
        try:
            ip = self.entry_ip.get().strip()
            port = int(self.entry_port.get().strip())
        except ValueError:
            messagebox.showerror("错误", "端口必须是数字！")
            return

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.server_socket.bind((ip, port))
            self.server_socket.listen(5)
        except Exception as e:
            messagebox.showerror("错误", f"启动失败：{str(e)}")
            return

        self.is_running = True
        self.btn_start.config(state=tk.DISABLED)
        self.btn_stop.config(state=tk.NORMAL)
        self.log(f"服务器启动成功：{ip}:{port}")

        threading.Thread(target=self.accept_clients, daemon=True).start()

    def stop_server(self):
        """停止服务器"""
        self.is_running = False
        if self.server_socket:
            try:
                self.server_socket.close()
            except:
                pass
        # 关闭所有客户端连接
        with self.clients_lock:
            for client in self.clients.keys():
                try:
                    client.send("服务器已关闭连接！".encode("utf-8"))
                    client.close()
                except:
                    pass
            self.clients.clear()
        self.btn_start.config(state=tk.NORMAL)
        self.btn_stop.config(state=tk.DISABLED)
        self.update_online_info()
        self.log("服务器已停止")

    def accept_clients(self):
        """监听并接受客户端连接（先接收用户名）"""
        while self.is_running:
            try:
                client_socket, client_addr = self.server_socket.accept()
                # 第一步：接收客户端发送的用户名（最多1024字节）
                try:
                    username = client_socket.recv(1024).decode("utf-8").strip()
                    if not username:  # 用户名不能为空
                        client_socket.send("用户名不能为空！连接被拒绝".encode("utf-8"))
                        client_socket.close()
                        self.log(f"拒绝连接 {client_addr}：用户名为空")
                        continue
                except:
                    client_socket.close()
                    self.log(f"拒绝连接 {client_addr}：获取用户名失败")
                    continue

                # 第二步：添加客户端信息
                with self.clients_lock:
                    self.clients[client_socket] = (client_addr, username)
                
                self.log(f"新客户端连接：{client_addr}（用户名：{username}）")
                self.update_online_info()
                # 通知所有客户端：新用户上线（包括本人）
                self.broadcast_message(f"📢 {username} 加入聊天！", exclude_client=None)
                # 通知当前客户端：连接成功
                client_socket.send(f"✅ 欢迎 {username}！已加入聊天".encode("utf-8"))

                # 启动处理该客户端消息的线程
                threading.Thread(target=self.handle_client, args=(client_socket, client_addr, username), daemon=True).start()
            except:
                if self.is_running:
                    self.log("接受客户端连接失败")
                break

    def handle_client(self, client_socket, client_addr, username):
        """处理单个客户端的消息"""
        while self.is_running:
            try:
                msg = client_socket.recv(1024).decode("utf-8")
                if not msg:  # 客户端关闭连接
                    break
                self.log(f"收到 {username}（{client_addr}）的消息：{msg}")
                # 关键修改：广播时排除发送者（不给本人发）
                self.broadcast_message(f"{username}：{msg}", exclude_client=client_socket)
            except:
                break

        # 客户端断开连接
        self.log(f"客户端断开连接：{username}（{client_addr}）")
        with self.clients_lock:
            if client_socket in self.clients:
                del self.clients[client_socket]
        try:
            client_socket.close()
        except:
            pass
        # 通知所有客户端：用户下线（包括本人，若还在线）
        self.broadcast_message(f"📢 {username} 离开聊天！", exclude_client=None)
        self.update_online_info()

    def broadcast_message(self, msg, exclude_client=None):
        """广播消息给所有客户端（可排除指定客户端）"""
        with self.clients_lock:
            # 遍历所有客户端socket（转列表避免遍历中修改字典）
            for client in list(self.clients.keys()):  
                if client == exclude_client:
                    continue  # 跳过排除的客户端（发送者）
                try:
                    client.send(msg.encode("utf-8"))
                except:
                    # 发送失败，移除该客户端
                    del self.clients[client]
                    client.close()

if __name__ == "__main__":
    win = tk.Tk()
    app = SocketServerGUI(win)
    win.mainloop()