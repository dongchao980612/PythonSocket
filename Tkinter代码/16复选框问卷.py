import tkinter as tk
from tkinter import messagebox

class CheckButtonLimitDemo:
    def __init__(self, win):
        self.win = win
        self.win.title("多个Checkbutton")
        self.win.geometry("400x550")

    
   
        self.check_vars = {
            "篮球": tk.BooleanVar(value=False),
            "足球": tk.BooleanVar(value=False),
            "羽毛球": tk.BooleanVar(value=False),
            "乒乓球": tk.BooleanVar(value=False),
            "游泳": tk.BooleanVar(value=False)
        }


        self.result_var = tk.StringVar(value="已选中：无")

        # 2. 创建布局
        self.frame_check = tk.Frame(win, relief=tk.GROOVE, bd=1, padx=20, pady=10)
        tk.Label(
            self.frame_check,
            text=f"请选择爱好：",
            font=("微软雅黑", 12),
            fg="#d9534f"
        ).pack(anchor=tk.W)

        # 批量创建Checkbutton
        for text, var in self.check_vars.items():
            cb = tk.Checkbutton(
                self.frame_check,
                text=text,
                variable=var,
                font=("微软雅黑", 11),
                command=self.check_limit  # 触发选中限制校验
            )
            cb.pack(anchor=tk.W, pady=5)

        self.frame_check.pack(pady=20)

        # ========== 核心修改：Label绑定StringVar ==========
        self.label_result = tk.Label(
            win,
            textvariable=self.result_var,  # 绑定StringVar
            font=("微软雅黑", 12)
        )
        self.label_result.pack(pady=10)

        # 4. 确认按钮
        tk.Button(
            win,
            text="确认选择",
            command=self.show_selected,
            font=("微软雅黑", 12),
            width=15
        ).pack(pady=10)

    def check_limit(self):
        """校验选中数量，超过限制则取消最后一次选择"""
        # 统计当前选中数量
        selected_count = sum(var.get() for var in self.check_vars.values())
        selected_text = [text for text, var in self.check_vars.items() if var.get()]

        # ========== 核心修改：用StringVar.set()更新文本 ==========
        # 更新结果标签（通过修改StringVar的值，Label自动同步）
        if selected_text:
            self.result_var.set(f"已选中：{', '.join(selected_text)}（共{selected_count}个）")
        else:
            self.result_var.set("已选中：无")



    def show_selected(self):
        """弹窗显示结果"""
        selected_text = [text for text, var in self.check_vars.items() if var.get()]
        if not selected_text:
            messagebox.showwarning("提示", "请至少选择一个爱好！")
        else:
            messagebox.showinfo("选择结果", f"你选中的爱好：\n{', '.join(selected_text)}")

if __name__ == "__main__":
    win = tk.Tk()
    app = CheckButtonLimitDemo(win)
    win.mainloop()