import tkinter as  tk
win = tk.Tk()
win.geometry("250x120+100+100")


win.title("Variable")

text_var = tk.StringVar(value="你好世界")
label = tk.Label(win,textvariable=text_var)
label.pack()  



entry = tk.Entry(win, textvariable=text_var, font=("微软雅黑", 12), width=30)
entry.pack(pady=10)

def  text_var_callback_fun(name, index, mode):
    print(f"当前值：{text_var.get()}")


text_var.trace_add("write",callback=text_var_callback_fun)


def change_var():
    text_var.set("变量被修改了！")  # 修改变量值

btn = tk.Button(win, text="修改变量值", command=change_var, font=("微软雅黑", 12))
btn.pack(pady=10)

win.mainloop()