import tkinter as tk
from tkinter import messagebox

value_to_text = {
    "A": "Python",
    "B": "C",
    "C": "Java"
}


def show_selected():
    """点击确认按钮，弹窗显示选中结果"""
    selected_value = text_var.get()
    # 映射值到对应的编程语言名称（提升用户体验）

    selected_text = value_to_text.get(selected_value, "无")
    messagebox.showinfo("选择结果", f"你选中的编程语言是：{selected_text}")


win = tk.Tk()
win.title("单选框")
win.geometry("300x320")  
win.resizable(False, False) 

# 2. 创建核心变量
# 单选框绑定的变量（StringVar），默认选中"A"（Python）
text_var = tk.StringVar(value="A")
# 结果展示的变量（StringVar），动态更新选中状态
result_var = tk.StringVar(value=f"当前选中：{value_to_text['A']}")


# 4. 创建界面布局
# 标题标签
tk.Label(
    win,
    text="请选择你熟悉的编程语言：",
    font=("微软雅黑", 12, "bold"),
    fg="#333333"
).pack(pady=15)
def choose_fun():
    current_value = text_var.get()
    result_var.set(f"当前选中：{value_to_text[current_value]}")

radio_frame = tk.Frame(win)
for index,value in enumerate(value_to_text.items()):
    tk.Radiobutton(
        radio_frame,
        text=value[1],
        variable=text_var,
        value=value[0],
        font=("微软雅黑", 11),
        fg="#0066cc",  # 文字颜色
        selectcolor="#e6f7ff",  # 选中时的背景色
        command=choose_fun
    ).pack(anchor=tk.W, pady=5)

radio_frame.pack(padx=30, anchor=tk.W)

# 结果展示标签（绑定result_var，动态更新）
tk.Label(
    win,
    textvariable=result_var,
    font=("微软雅黑", 11),
    fg="#d9534f"  # 红色突出显示结果
).pack(pady=20)

# 确认按钮（触发弹窗展示结果）
tk.Button(
    win,
    text="确认选择",
    command=show_selected,
    font=("微软雅黑", 11),
    width=15,
    bg="#5cb85c",
    fg="white",
    relief=tk.RAISED,
    bd=1
).pack(pady=10)

# 启动主循环
win.mainloop()