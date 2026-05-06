import tkinter as  tk
win = tk.Tk()
win.geometry("250x120+100+100")


win.title("标签组件")


label = tk.Label(win,text="你好,世界")
label1 = tk.Label(win,text="你好,世界1")
label2 = tk.Label(win,text="你好,世界2")

# label2.pack()
# label1.pack()
# label.pack()


label = tk.Label(
    win,                # 必选：父组件（窗口）
    text="你好,世界",    # 核心：显示的文本
    font=("楷体", 18, "bold"),  # 字体：微软雅黑、14号、加粗
    fg="#ADD8E6",         # 文本颜色：白色
    bg="#DA70D6",       # 背景颜色：蓝色（十六进制）
    padx=10,            # 水平内边距20px
    pady=10             # 垂直内边距10px
)
label.pack()


win.mainloop()