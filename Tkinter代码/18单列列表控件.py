import tkinter as tk
from tkinter import messagebox

def on_select(event):
    """选中列表项时触发的事件"""
    selected_indices = listbox.curselection()
    if not selected_indices:
        return
    # 获取选中项的文本
    selected_text = listbox.get(selected_indices[0])
    label.config(text=f"当前选中：{selected_text}")

def add_item():
    """添加列表项"""
    text = entry.get().strip()
    if not text:
        messagebox.showwarning("提示", "输入不能为空！")
        return
    listbox.insert(tk.END, text)  # 在列表末尾添加
    entry.delete(0, tk.END)  # 清空输入框

def del_item():
    """删除选中的列表项"""
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showwarning("提示", "请先选中要删除的项！")
        return
    # 从后往前删（避免索引错乱）
    for idx in reversed(selected_indices):
        listbox.delete(idx)

# 创建主窗口
win = tk.Tk()
win.title("Tkinter Listbox")
win.geometry("800x350")


listbox = tk.Listbox(
    win,
    font=("微软雅黑", 11),
    selectmode=tk.SINGLE, 
    width=30,
    height=10
)
# 绑定选中事件（对应Qt的itemClicked信号）
listbox.bind("<<ListboxSelect>>", on_select)


init_items = ["Python", "Java", "C++", "Go", "JavaScript"]
for item in init_items:
    listbox.insert(tk.END, item)


listbox.pack(side=tk.LEFT, padx=20, pady=20)

# 5. 操作按钮 + 输入框
frame_oper = tk.Frame(win)
entry = tk.Entry(frame_oper, font=("微软雅黑", 11), width=15)
entry.pack(side=tk.LEFT, padx=5, pady=5)

tk.Button(frame_oper, text="添加", command=add_item, font=("微软雅黑", 10)).pack(side=tk.LEFT, padx=5)
tk.Button(frame_oper, text="删除", command=del_item, font=("微软雅黑", 10)).pack(side=tk.LEFT, padx=5)
frame_oper.pack(pady=10)

# 6. 选中结果标签
label = tk.Label(win, text="当前选中：Python", font=("微软雅黑", 11))
label.pack(pady=10)

win.mainloop()