import tkinter as  tk

win = tk.Tk()
win.geometry("250x120+100+100")

win.title("按钮组件")


def click_action():
    print("登录...")
    btn.config(text="按钮被点击了！", bg="#ff6600")  # 更新标签文本和背景色


btn = tk.Button(
    win,  # 必选：父组件（窗口）
    text="点我",  # 核心：按钮显示文本
    font=("微软雅黑", 12),  # 字体样式
    bg="#0099ff",  # 按钮背景色（蓝色）
    fg="white",  # 文本颜色（白色）
    width=10,  # 按钮宽度
    height=1,  # 按钮高度
    command=click_action  # 绑定点击事件：执行click_action函数
)
btn.pack()

win.mainloop()
