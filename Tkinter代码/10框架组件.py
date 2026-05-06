import tkinter as tk
from tkinter import messagebox


def get_input():
    """获取输入框Frame中的内容"""
    username = entry_user.get().strip()
    password = entry_pwd.get().strip()
    if not username or not password:
        messagebox.showwarning("提示", "用户名/密码不能为空！")
        return
    messagebox.showinfo("输入内容", f"用户名：{username}\n密码：{password}")

# 创建主窗口
win = tk.Tk()
win.title("Frame 组件详解")
win.geometry("500x350+300+200")
win.resizable(False, False)

#  嵌套Frame：输入框分组（Frame嵌套Frame）

# 外层Frame：包裹整个输入区域
input_main_frame = tk.Frame(win, bg="#ffffff", relief=tk.RAISED, bd=0)
other_main_frame  =tk.Frame(win,bg="black")

# 内层Frame1：用户名分组
user_frame = tk.Frame(input_main_frame, bg="#dc1010")
label_user = tk.Label(user_frame, text="用户名：", bg="#ffffff", font=("微软雅黑", 11))
entry_user = tk.Entry(user_frame, font=("微软雅黑", 11), width=20)
label_user.pack(side=tk.LEFT, padx=5, pady=10)
entry_user.pack(side=tk.LEFT, padx=5, pady=10)

# 内层Frame2：密码分组
pwd_frame = tk.Frame(input_main_frame, bg="#b32ed1")
label_pwd = tk.Label(pwd_frame, text="密  码：", bg="#ffffff", font=("微软雅黑", 11))
entry_pwd = tk.Entry(pwd_frame, font=("微软雅黑", 11), width=20, show="*")
label_pwd.pack(side=tk.LEFT, padx=5, pady=10)
entry_pwd.pack(side=tk.LEFT, padx=5, pady=10)

# 内层Frame3：按钮分组
btn_frame = tk.Frame(input_main_frame, bg="#1ECA93")
btn_get = tk.Button(btn_frame, text="获取内容", command=get_input, font=("微软雅黑", 10))
btn_clear = tk.Button(btn_frame, text="清空内容", command=lambda: (entry_user.delete(0, tk.END), entry_pwd.delete(0, tk.END)), font=("微软雅黑", 10))
btn_get.pack(side=tk.LEFT, padx=10, pady=10)
btn_clear.pack(side=tk.LEFT, padx=10, pady=10)

# 布局内层Frame到外层Frame
user_frame.pack()
pwd_frame.pack()
btn_frame.pack()


user_frame = tk.Frame(other_main_frame, bg="#dc1010")
label_user = tk.Label(user_frame, text="用户名：", bg="#054916", font=("微软雅黑", 11))
entry_user = tk.Entry(user_frame, font=("微软雅黑", 11), width=20)
label_user.pack(side=tk.LEFT, padx=5, pady=10)
entry_user.pack(side=tk.LEFT, padx=5, pady=10)
user_frame.pack()

input_main_frame.pack(pady=20, fill=tk.X, padx=50)
other_main_frame.pack(pady=20, fill=tk.X, padx=100)
# 启动主循环
win.mainloop()