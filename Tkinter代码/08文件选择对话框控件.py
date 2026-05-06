import tkinter as  tk
from tkinter import filedialog
win = tk.Tk()
win.geometry("250x120+100+100")


win.title("文件选择对话框控件")

def click_action():
    file_path = filedialog.askopenfilename(title="选择文本文件",filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])
    print(file_path)
    
btn = tk.Button(
    win,              
    text="打开",        

    command=click_action  # 绑定点击事件：执行click_action函数
)
btn.pack()  

win.mainloop()