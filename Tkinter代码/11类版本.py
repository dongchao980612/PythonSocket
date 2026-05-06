import tkinter as tk
from tkinter import messagebox

class MyLoginGUI:
    def __init__(self, win,title,size):
        self.win = win
        self.win.title(title)
        self.win.geometry(size)
        self.win.resizable(False, False)

        #  嵌套Frame：输入框分组（Frame嵌套Frame）

        # 外层Frame：包裹整个输入区域
        self.input_main_frame = tk.Frame(self.win, bg="#ffffff", relief=tk.RAISED, bd=0)
        # 内层Frame1：用户名分组
        self.user_frame = tk.Frame(self.input_main_frame, bg="#dc1010")
        self.label_user = tk.Label(self.user_frame, text="用户名：", bg="#ffffff", font=("微软雅黑", 11))
        self.entry_user = tk.Entry(self.user_frame, font=("微软雅黑", 11), width=20)
        self.label_user.pack(side=tk.LEFT, padx=5, pady=10)
        self.entry_user.pack(side=tk.LEFT, padx=5, pady=10)

        # 内层Frame2：密码分组
        self.pwd_frame = tk.Frame(self.input_main_frame, bg="#b32ed1")
        self.label_pwd = tk.Label(self.pwd_frame, text="密  码：", bg="#ffffff", font=("微软雅黑", 11))
        self.entry_pwd = tk.Entry(self.pwd_frame, font=("微软雅黑", 11), width=20, show="*")
        self.label_pwd.pack(side=tk.LEFT, padx=5, pady=10)
        self.entry_pwd.pack(side=tk.LEFT, padx=5, pady=10)

        # 内层Frame3：按钮分组
        self.btn_frame = tk.Frame(self.input_main_frame, bg="#1ECA93")
        self.btn_get = tk.Button(self.btn_frame, text="获取内容", command=self.get_input, font=("微软雅黑", 10))
        self.btn_clear = tk.Button(self.btn_frame, text="清空内容", command=lambda: (self.entry_user.delete(0, tk.END), self.entry_pwd.delete(0, tk.END)), font=("微软雅黑", 10))
        self.btn_get.pack(side=tk.LEFT, padx=10, pady=10)
        self.btn_clear.pack(side=tk.LEFT, padx=10, pady=10)

        # 布局内层Frame到外层Frame
        self.user_frame.pack()
        self.pwd_frame.pack()
        self.btn_frame.pack()

        self.input_main_frame.pack(pady=20, fill=tk.X, padx=50)

    def get_input(self):
        """获取输入框Frame中的内容"""
        username = self.entry_user.get().strip()
        password = self.entry_pwd.get().strip()
        if not username or not password:
            messagebox.showwarning("提示", "用户名/密码不能为空！")
            return
        messagebox.showinfo("输入内容", f"用户名：{username}\n密码：{password}")


if __name__ == "__main__":
    win = tk.Tk()
    app = MyLoginGUI(win,"登录界面","600x500")
    win.mainloop()


