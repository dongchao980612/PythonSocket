import tkinter as tk
from tkinter import ttk, messagebox

def on_table_select(event):
    """选中表格行时触发的事件"""
    # 获取选中的行ID
    selected_items = tree.selection()
    if not selected_items:
        return
    # 获取行数据（item方法返回字典，values是列值列表）
    row_data = tree.item(selected_items[0])["values"]
    label.config(text=f"选中行：{row_data}")

def add_row():
    """由用户输入内容添加表格行（核心修改）"""
    # 1. 获取用户输入并去除首尾空格
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    gender = entry_gender.get().strip()

    # 2. 输入校验
    # 校验姓名非空
    if not name:
        messagebox.showwarning("输入提示", "姓名不能为空！")
        entry_name.focus()  # 聚焦到姓名输入框
        return
    # 校验年龄是数字且合理
    if not age.isdigit():
        messagebox.showwarning("输入提示", "年龄必须是数字！")
        entry_age.focus()
        entry_age.select_range(0, tk.END)  # 选中错误输入，方便用户修改
        return
    age = int(age)
    if age < 0 or age > 150:
        messagebox.showwarning("输入提示", "年龄需在0-150之间！")
        entry_age.focus()
        entry_age.select_range(0, tk.END)
        return
    # 校验性别非空
    if not gender:
        messagebox.showwarning("输入提示", "性别不能为空！")
        entry_gender.focus()
        return

    # 3. 插入新行到表格
    tree.insert("", tk.END, values=(name, age, gender))

    # 4. 清空输入框，聚焦到姓名框（方便继续添加）
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_name.focus()

def del_row():
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showwarning("操作提示", "请先选中要删除的行！")
        return
    for item in selected_items:
        tree.delete(item)

# 创建主窗口
win = tk.Tk()
win.title("Tkinter Treeview（对应Qt TableWidget）")
# win.geometry("500x350")

# 创建Treeview（配置为表格模式）
tree = ttk.Treeview(
    win,
    columns=("name", "age", "gender"),  # 定义列名
    show="headings",  # 只显示表头（隐藏树形的根节点）
    height=8
)

# 设置表头
tree.heading("name", text="姓名")
tree.heading("age", text="年龄")
tree.heading("gender", text="性别")

# 设置列宽
tree.column("name", width=150, anchor=tk.CENTER)
tree.column("age", width=100, anchor=tk.CENTER)
tree.column("gender", width=100, anchor=tk.CENTER)

# 绑定选中事件（对应Qt的itemClicked信号）
tree.bind("<<TreeviewSelect>>", on_table_select)



# 初始化表格数据
init_data = [
    ("张三", 25, "男"),
    ("李四", 22, "女"),
    ("王五", 30, "男")
]
for row in init_data:
    tree.insert("", tk.END, values=row)



# 操作按钮
input_frame = tk.Frame(win)
# 姓名输入框
tk.Label(input_frame, text="姓名：", font=("微软雅黑", 11)).grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(input_frame, font=("微软雅黑", 11), width=10)
entry_name.grid(row=0, column=1, padx=5, pady=5)

# 年龄输入框
tk.Label(input_frame, text="年龄：", font=("微软雅黑", 11)).grid(row=0, column=2, padx=5, pady=5)
entry_age = tk.Entry(input_frame, font=("微软雅黑", 11), width=10)
entry_age.grid(row=0, column=3, padx=5, pady=5)

# 性别输入框
tk.Label(input_frame, text="性别：", font=("微软雅黑", 11)).grid(row=0, column=4, padx=5, pady=5)
entry_gender = tk.Entry(input_frame, font=("微软雅黑", 11), width=10)
entry_gender.grid(row=0, column=5, padx=5, pady=5)

tk.Button(input_frame, text="添加行", command=add_row, font=("微软雅黑", 11), bg="#5cb85c", fg="white").grid(row=0, column=6, padx=10, pady=5)
tk.Button(input_frame, text="删除行", command=del_row, font=("微软雅黑", 11), bg="#d9534f", fg="white").grid(row=0, column=7, padx=10, pady=5)
input_frame.pack(pady=10)

# 选中结果标签
label = tk.Label(win, text="选中行：无", font=("微软雅黑", 11))
label.pack(pady=10)

# 布局（表格 + 滚动条）
tree.pack(side=tk.LEFT, padx=20, pady=20)
input_frame.pack(side=tk.BOTTOM, pady=10)

win.mainloop()