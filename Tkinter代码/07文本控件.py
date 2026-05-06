import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("文本控件")

def get_all_text():
    """获取全部文本"""
    content = text.get(1.0, tk.END).strip()  # strip()去除末尾换行
    if not content:
        messagebox.showwarning("提示", "文本框为空！")
        return
    messagebox.showinfo("文本内容", content)

def clear_all_text():
    """清空全部文本"""
    text.delete(1.0, tk.END)

btn_get = tk.Button(win, text="获取全部文本", font=("微软雅黑", 10), command=get_all_text)
btn_clear = tk.Button(win, text="清空文本", font=("微软雅黑", 10), command=clear_all_text)
btn_get.pack(side=tk.TOP, padx=15)
btn_clear.pack(side=tk.TOP, padx=5)



# 创建Text，绑定滚动条
text = tk.Text(
    win,
    font=("微软雅黑", 11),
    width=50,
    height=15,
    wrap=tk.WORD,  # 按单词换行
)
text.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

# 4. 启动主循环
win.mainloop()