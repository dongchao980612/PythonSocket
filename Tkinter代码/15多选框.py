import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("多选框")

def click_fun():
    print(bool_var.get())

bool_var=tk.BooleanVar()

def  bool_var_callback_fun(name, index, mode):
    print(f"当前值：{bool_var.get()}")
bool_var.trace_add("write",callback=bool_var_callback_fun)

checkbtn = tk.Checkbutton( win,text="多选框",command=click_fun,variable=bool_var)
checkbtn.pack()

# 4. 启动主循环
win.mainloop()