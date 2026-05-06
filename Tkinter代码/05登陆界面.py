import tkinter as  tk
from tkinter import messagebox
win = tk.Tk()
win.geometry("400x150+400+200")
win.resizable(False, False)

win.title("输入框组件")

# 3.1 普通输入框（用户名）
username_label = tk.Label(win, text="用户名", font=("微软雅黑", 11))
username_entry = tk.Entry(
    win,
    font=("微软雅黑", 11),
    width=25,
    fg="red",
    bg="#f8f8f8",
    justify=tk.LEFT  # 文本左对齐
)

# 3.2 密码输入框
pwd_label = tk.Label(win, text="密码", font=("微软雅黑", 11))
pwd_entry = tk.Entry(
    win,
    font=("微软雅黑", 11),
    width=25,
    show="*"  # 输入内容显示为*
)



def login_fun():
    # 获取输入框内容（strip() 去除首尾空格）
    username = username_entry.get().strip()
    password = pwd_entry.get().strip()
    
    # 基础验证逻辑（实际开发中需对接数据库/接口）
    if username == "admin" and password == "123456":
        messagebox.showinfo("成功", "登录成功！欢迎使用")
        # 登录成功后可执行其他操作（如打开新窗口、关闭当前窗口等）
    else:
        # 验证失败提示
        messagebox.showerror("失败", "用户名或密码错误！")
        # 清空密码输入框
        pwd_entry.delete(0, tk.END)

def register_fun():
    messagebox.showinfo("提示", "注册功能待开发...")


# 4. 创建功能按钮
btn_get = tk.Button(win, text="登录", font=("微软雅黑", 10), width=10, command=login_fun)
btn_clear = tk.Button(win, text="注册", font=("微软雅黑", 10), width=10, command=register_fun)

username_label.grid(row=0, column=0, padx=10, pady=15, sticky="w")
username_entry.grid(row=0, column=1, pady=15)

pwd_label.grid(row=1, column=0, padx=10, sticky="w")
pwd_entry.grid(row=1, column=1)


btn_get.grid(row=3, column=0, padx=5, pady=10)
btn_clear.grid(row=3, column=1, padx=5, pady=10, sticky="w")


win.mainloop()