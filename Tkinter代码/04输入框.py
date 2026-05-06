import tkinter as  tk
win = tk.Tk()
win.geometry("400x350+400+200")


win.title("输入框组件")

# 普通输入框（用户名）
label_normal = tk.Label(win, text="普通输入框：", font=("微软雅黑", 11))
entry_normal = tk.Entry(
    win,
    font=("微软雅黑", 11),
    width=25,
    fg="#333",
    bg="#f8f8f8",
    justify=tk.LEFT  # 文本左对齐
)

# 密码输入框
label_pwd = tk.Label(win, text="密码输入框：", font=("微软雅黑", 11))
entry_pwd = tk.Entry(
    win,
    font=("微软雅黑", 11),
    width=25,
    show="*"  # 输入内容显示为*
)

# 只读输入框
label_readonly = tk.Label(win, text="只读输入框：", font=("微软雅黑", 11))
entry_readonly = tk.Entry(
    win,
    font=("微软雅黑", 11),
    width=25,
    state="readonly"  # 只读状态（无法输入，可通过代码修改）
)

def get_content():
    print("普通输入框内容：", entry_normal.get())
    print("密码输入框内容：", entry_pwd.get())
    print("只读输入框内容：", entry_readonly.get())
    # clear_content()  # 获取内容后清空输入框

def clear_content():
    """清空所有输入框"""
    entry_normal.delete(0, tk.END)  # 0表示起始位置，tk.END表示末尾
    entry_pwd.delete(0, tk.END)
    entry_readonly.delete(0, tk.END)  # 只读状态需先解锁再清空
def insert_default():
    """插入默认文本到普通输入框"""
    # entry_normal.insert(0, "请输入用户名")  # 在开头插入
    entry_normal.insert(tk.END, "后缀")  # 在末尾插入
def switch_state():
    """切换输入框状态（禁用/启用）"""
    print(entry_normal.keys())
    if entry_normal["state"] == tk.NORMAL:
        entry_normal.config(state=tk.DISABLED)
        entry_pwd.config(state=tk.DISABLED)
        btn_switch.config(text="启用输入框")
    else:
        entry_normal.config(state=tk.NORMAL)
        entry_pwd.config(state=tk.NORMAL)
        btn_switch.config(text="禁用输入框")

# 创建功能按钮
btn_get = tk.Button(win, text="获取内容", font=("微软雅黑", 10), width=10, command=get_content)
btn_clear = tk.Button(win, text="清空内容", font=("微软雅黑", 10), width=10, command=clear_content)
btn_insert = tk.Button(win, text="插入默认值", font=("微软雅黑", 10), width=10, command=insert_default)
btn_switch = tk.Button(win, text="禁用输入框", font=("微软雅黑", 10), width=10, command=switch_state)

label_normal.grid(row=0, column=0, padx=10, pady=15, sticky="w")
entry_normal.grid(row=0, column=1, pady=15)

label_pwd.grid(row=1, column=0, padx=10, sticky="w")
entry_pwd.grid(row=1, column=1)

label_readonly.grid(row=2, column=0, padx=10, pady=15, sticky="w")
entry_readonly.grid(row=2, column=1, pady=15)

btn_get.grid(row=3, column=0, padx=5, pady=10)
btn_clear.grid(row=3, column=1, padx=5, pady=10, sticky="w")
btn_insert.grid(row=4, column=0, padx=5, pady=5)
btn_switch.grid(row=4, column=1, padx=5, pady=5, sticky="w")

win.mainloop()