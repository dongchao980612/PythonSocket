import os
import tkinter as  tk
from tkinter import filedialog
from tkinter import messagebox

win = tk.Tk()


win.title("文本编辑器 - 未保存")
win.geometry("600x400+300+200")


current_file_path = ""
def new_text_file():
    global current_file_path
    # 第一步：检查是否有未保存的内容
    content = text.get(1.0, tk.END).rstrip("\n")
    if content:  # 文本不为空，说明有未保存内容
        # 弹出确认框：保存(S)/不保存(N)/取消(C)
        choice = messagebox.askyesnocancel(
            "提示",
            "当前有未保存的内容，是否先保存？\n【是】=保存后新建 【否】=直接新建 【取消】=放弃新建"
        )
        # 分支1：用户点击“取消”
        if choice is None:
            return
        # 分支2：用户点击“是”（先保存，再新建）
        elif choice:
            # 调用保存函数，若保存失败则终止新建
            save_success = save_fun_for_new()
            if not save_success:
                return
        # 分支3：用户点击“否”（直接新建，不保存）→ 无需额外操作
    
    # 第二步：执行新建逻辑
    text.delete(1.0, tk.END)  # 清空Text控件
    current_file_path = ""    # 重置全局文件路径
    win.title("文本编辑器 - 未保存")  # 恢复窗口标题
    text.focus()  # 光标定位到Text，方便用户直接编辑

# 辅助函数：供新建时调用的保存逻辑（返回保存是否成功）
def save_fun_for_new():
    global current_file_path
    content = text.get(1.0, tk.END).rstrip("\n")
    # 已有文件路径：直接保存
    if current_file_path:
        try:
            with open(current_file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        except Exception as e:
            messagebox.showerror("错误", f"保存失败：{str(e)}")
            return False
    # 无文件路径：弹出另存为
    else:
        save_path = filedialog.asksaveasfilename(
            title="另存为",
            defaultextension=".txt",
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
        )
        if not save_path:  # 用户取消保存
            return False
        try:
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(content)
            current_file_path = save_path
            win.title(f"已保存：{os.path.basename(save_path)} - 文本编辑器")
            return True
        except Exception as e:
            messagebox.showerror("错误", f"保存失败：{str(e)}")
            return False

# 2. 打开文本文件函数（复用之前的逻辑）
def open_text_file():
    global current_file_path
    # 先检查未保存内容（和新建逻辑一致）
    content = text.get(1.0, tk.END).rstrip("\n")
    if content:
        choice = messagebox.askyesnocancel("提示", "当前有未保存的内容，是否先保存？")
        if choice is None:
            return
        elif choice:
            if not save_fun_for_new():
                return
    # 弹出文件选择框
    file_path = filedialog.askopenfilename(
        title="选择文本文件",
        filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
    )
    if not file_path:
        return
    if not os.path.exists(file_path):
        messagebox.showerror("错误", "所选文件不存在！")
        return
    # 读取文件内容
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, "r", encoding="gbk") as f:
                content = f.read()
        except Exception as e:
            messagebox.showerror("错误", f"读取失败：{str(e)}")
            return
    except Exception as e:
        messagebox.showerror("错误", f"读取失败：{str(e)}")
        return
    # 更新Text和全局变量
    text.delete(1.0, tk.END)
    text.insert(1.0, content)
    current_file_path = file_path
    win.title(f"已打开：{os.path.basename(file_path)} - 文本编辑器")
    
#  打开文本文件函数
def open_text_file():
    global current_file_path  # 声明使用全局变量
    # 弹出文件选择对话框
    file_path = filedialog.askopenfilename(
        title="选择文本文件",
        filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
    )
    if not file_path:
        return
    # 检查文件是否存在
    if not os.path.exists(file_path):
        messagebox.showerror("错误", "所选文件不存在！")
        return
    # 读取文件内容（兼容编码）
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, "r", encoding="gbk") as f:
                content = f.read()
        except Exception as e:
            messagebox.showerror("错误", f"读取文件失败：{str(e)}")
            return
    except Exception as e:
        messagebox.showerror("错误", f"读取文件失败：{str(e)}")
        return
    # 更新Text和全局文件路径
    text.delete(1.0, tk.END)
    text.insert(1.0, content)
    current_file_path = file_path  # 记录当前文件路径
    win.title(f"已打开：{os.path.basename(file_path)} - 文本编辑器")  # 更新窗口标题

def save_text_file():
    global current_file_path
    # 获取Text中的内容
    content = text.get(1.0, tk.END).rstrip("\n")  # 去除末尾多余换行符
    if not content:
        messagebox.showwarning("提示", "文本内容为空，无需保存！")
        return
    
    # 情况1：已有打开的文件路径（直接覆盖保存）
    if current_file_path:
        try:
            with open(current_file_path, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("成功", f"已保存到：{current_file_path}")
        except Exception as e:
            messagebox.showerror("错误", f"保存失败：{str(e)}")
    # 情况2：无文件路径（弹出“另存为”对话框）
    else:
        save_path = filedialog.asksaveasfilename(
            title="另存为",
            defaultextension=".txt",  # 默认后缀为.txt
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
        )
        if not save_path:  # 用户取消保存
            return
        try:
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(content)
            current_file_path = save_path  # 更新全局文件路径
            win.title(f"已保存：{os.path.basename(save_path)} - 文本编辑器")
            messagebox.showinfo("成功", f"已保存到：{save_path}")
        except Exception as e:
            messagebox.showerror("错误", f"保存失败：{str(e)}")


def exit_fun():
    win.quit()

main_menu = tk.Menu(win)
sub_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="文件", menu=sub_menu)
sub_menu.add_command(label="新建", command=new_text_file)
sub_menu.add_command(label="打开", command=open_text_file)
sub_menu.add_command(label="保存", command=save_text_file)
sub_menu.add_separator()  
sub_menu.add_command(label="退出", command=exit_fun)

text = tk.Text(
    win,
    font=("微软雅黑", 11),
    width=50,
    height=15,
    wrap=tk.WORD,  # 按单词换行
)
text.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

win.config(menu=main_menu)

win.mainloop()