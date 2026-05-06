import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv
import re
from datetime import datetime

# ---------------------- 全局数据（管理员账号） ----------------------
ADMIN_ACCOUNTS = [
    {"username": "admin", "password": "123456", "phone": "13800138000"}
]

# ---------------------- 工具函数 ----------------------
def is_valid_phone(phone):
    if not phone:
        return True
    pattern = r'^1[3-9]\d{9}$'
    return re.match(pattern, phone) is not None

def is_valid_student_id(sid):
    return sid.isdigit() and len(sid) == 8

def is_username_exist(username):
    return any(admin["username"] == username for admin in ADMIN_ACCOUNTS)

# ---------------------- 注册窗口类（核心修改：接收LoginWindow实例） ----------------------
class RegisterWindow:
    def __init__(self, login_window):  # 修改1：接收LoginWindow实例，而非根窗口
        self.login_window = login_window  # 保存LoginWindow实例引用
        self.top = tk.Toplevel(login_window.master)  # 基于登录窗口的根窗口创建弹窗
        self.top.title("学生管理系统 - 注册")
        self.top.geometry("400x400")
        self.top.resizable(False, False)
        self.top.transient(login_window.master)
        self.top.grab_set()

        # 注册表单布局（无修改）
        frame = tk.Frame(self.top, padx=50, pady=30)
        tk.Label(frame, text="管理员注册", font=("微软雅黑", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=20)
        
        tk.Label(frame, text="账号：", font=("微软雅黑", 12)).grid(row=1, column=0, sticky=tk.W, pady=10)
        self.entry_user = tk.Entry(frame, font=("微软雅黑", 12), width=20)
        self.entry_user.grid(row=1, column=1, pady=10)
        self.entry_user.focus()

        tk.Label(frame, text="密码（≥6位）：", font=("微软雅黑", 12)).grid(row=2, column=0, sticky=tk.W, pady=10)
        self.entry_pwd = tk.Entry(frame, font=("微软雅黑", 12), width=20, show="*")
        self.entry_pwd.grid(row=2, column=1, pady=10)

        tk.Label(frame, text="确认密码：", font=("微软雅黑", 12)).grid(row=3, column=0, sticky=tk.W, pady=10)
        self.entry_pwd_confirm = tk.Entry(frame, font=("微软雅黑", 12), width=20, show="*")
        self.entry_pwd_confirm.grid(row=3, column=1, pady=10)

        tk.Label(frame, text="手机号（可选）：", font=("微软雅黑", 12)).grid(row=4, column=0, sticky=tk.W, pady=10)
        self.entry_phone = tk.Entry(frame, font=("微软雅黑", 12), width=20)
        self.entry_phone.grid(row=4, column=1, pady=10)

        btn_frame = tk.Frame(frame)
        tk.Button(btn_frame, text="注册", command=self.register, font=("微软雅黑", 12), 
                  bg="#5cb85c", fg="white", width=10).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="取消", command=self.top.destroy, font=("微软雅黑", 12), 
                  bg="#d9534f", fg="white", width=10).pack(side=tk.LEFT, padx=10)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=20)
        
        frame.pack()

    def register(self):
        """注册逻辑（修改2：访问LoginWindow的entry_user）"""
        username = self.entry_user.get().strip()
        pwd = self.entry_pwd.get().strip()
        pwd_confirm = self.entry_pwd_confirm.get().strip()
        phone = self.entry_phone.get().strip()

        # 校验规则（无修改）
        if not username:
            messagebox.showwarning("输入错误", "账号不能为空！")
            self.entry_user.focus()
            return
        if is_username_exist(username):
            messagebox.showwarning("输入错误", "账号已存在！")
            self.entry_user.focus()
            return
        if len(pwd) < 6:
            messagebox.showwarning("输入错误", "密码长度不能少于6位！")
            self.entry_pwd.focus()
            return
        if pwd != pwd_confirm:
            messagebox.showwarning("输入错误", "两次密码不一致！")
            self.entry_pwd_confirm.focus()
            return
        if not is_valid_phone(phone):
            messagebox.showwarning("输入错误", "手机号格式错误！")
            self.entry_phone.focus()
            return

        # 注册成功
        ADMIN_ACCOUNTS.append({
            "username": username,
            "password": pwd,
            "phone": phone if phone else "未填写"
        })
        messagebox.showinfo("注册成功", "管理员账号注册成功！请返回登录页登录。")
        self.top.destroy()
        # 修改3：通过login_window实例访问entry_user，而非self.master
        self.login_window.entry_user.delete(0, tk.END)
        self.login_window.entry_pwd.delete(0, tk.END)
        self.login_window.entry_user.focus()

# ---------------------- 登录窗口类（修改4：修正open_register方法） ----------------------
class LoginWindow:
    def __init__(self, master):
        self.master = master  # 根窗口
        self.master.title("学生管理系统 - 登录")
        self.master.geometry("400x350")
        self.master.resizable(False, False)

        # 登录表单（无修改）
        frame = tk.Frame(self.master, padx=50, pady=50)
        tk.Label(frame, text="管理员登录", font=("微软雅黑", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=20)
        
        tk.Label(frame, text="账号：", font=("微软雅黑", 12)).grid(row=1, column=0, sticky=tk.W, pady=10)
        self.entry_user = tk.Entry(frame, font=("微软雅黑", 12), width=20)
        self.entry_user.grid(row=1, column=1, pady=10)
        self.entry_user.insert(0, "admin")

        tk.Label(frame, text="密码：", font=("微软雅黑", 12)).grid(row=2, column=0, sticky=tk.W, pady=10)
        self.entry_pwd = tk.Entry(frame, font=("微软雅黑", 12), width=20, show="*")
        self.entry_pwd.grid(row=2, column=1, pady=10)
        self.entry_pwd.insert(0, "123456")

        # 登录 + 注册按钮（无修改）
        btn_frame = tk.Frame(frame)
        tk.Button(btn_frame, text="登录", command=self.login, font=("微软雅黑", 12), 
                  bg="#5cb85c", fg="white", width=10).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="注册", command=self.open_register, font=("微软雅黑", 12), 
                  bg="#337ab7", fg="white", width=10).pack(side=tk.LEFT, padx=10)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        frame.pack()

    def login(self):
        """登录验证（无修改）"""
        user = self.entry_user.get().strip()
        pwd = self.entry_pwd.get().strip()
        for admin in ADMIN_ACCOUNTS:
            if admin["username"] == user and admin["password"] == pwd:
                self.master.destroy()
                root = tk.Tk()
                MainWindow(root)
                root.mainloop()
                return
        messagebox.showerror("登录失败", "账号或密码错误！")

    def open_register(self):
        """修改5：传递LoginWindow实例（self），而非根窗口"""
        RegisterWindow(self)  # 关键修复：self是LoginWindow实例，包含entry_user属性

# ---------------------- 以下代码无修改 ----------------------
class StudentFormWindow:
    def __init__(self, master, callback, edit_data=None):
        self.master = master
        self.callback = callback
        self.edit_data = edit_data

        self.top = tk.Toplevel(master)
        self.top.title("编辑学生信息" if edit_data else "新增学生信息")
        self.top.geometry("450x400")
        self.top.resizable(False, False)
        self.top.transient(master)
        self.top.grab_set()

        frame = tk.Frame(self.top, padx=30, pady=20)
        
        tk.Label(frame, text="学号（8位数字）：", font=("微软雅黑", 11)).grid(row=0, column=0, sticky=tk.W, pady=8)
        self.entry_sid = tk.Entry(frame, font=("微软雅黑", 11), width=25)
        self.entry_sid.grid(row=0, column=1, pady=8)
        
        tk.Label(frame, text="姓名：", font=("微软雅黑", 11)).grid(row=1, column=0, sticky=tk.W, pady=8)
        self.entry_name = tk.Entry(frame, font=("微软雅黑", 11), width=25)
        self.entry_name.grid(row=1, column=1, pady=8)
        
        tk.Label(frame, text="性别：", font=("微软雅黑", 11)).grid(row=2, column=0, sticky=tk.W, pady=8)
        self.var_gender = tk.StringVar(value="男")
        tk.Radiobutton(frame, text="男", variable=self.var_gender, value="男", font=("微软雅黑", 11)).grid(row=2, column=1, sticky=tk.W)
        tk.Radiobutton(frame, text="女", variable=self.var_gender, value="女", font=("微软雅黑", 11)).grid(row=2, column=2, sticky=tk.W)
        
        tk.Label(frame, text="年龄（0-100）：", font=("微软雅黑", 11)).grid(row=3, column=0, sticky=tk.W, pady=8)
        self.entry_age = tk.Entry(frame, font=("微软雅黑", 11), width=25)
        self.entry_age.grid(row=3, column=1, pady=8)
        
        tk.Label(frame, text="班级：", font=("微软雅黑", 11)).grid(row=4, column=0, sticky=tk.W, pady=8)
        self.entry_class = tk.Entry(frame, font=("微软雅黑", 11), width=25)
        self.entry_class.grid(row=4, column=1, pady=8)
        
        tk.Label(frame, text="手机号：", font=("微软雅黑", 11)).grid(row=5, column=0, sticky=tk.W, pady=8)
        self.entry_phone = tk.Entry(frame, font=("微软雅黑", 11), width=25)
        self.entry_phone.grid(row=5, column=1, pady=8)
        
        tk.Label(frame, text="爱好：", font=("微软雅黑", 11)).grid(row=6, column=0, sticky=tk.W, pady=8)
        self.var_hobby1 = tk.BooleanVar(value=False)
        self.var_hobby2 = tk.BooleanVar(value=False)
        self.var_hobby3 = tk.BooleanVar(value=False)
        hobby_frame = tk.Frame(frame)
        tk.Checkbutton(hobby_frame, text="运动", variable=self.var_hobby1, font=("微软雅黑", 11)).pack(side=tk.LEFT, padx=5)
        tk.Checkbutton(hobby_frame, text="阅读", variable=self.var_hobby2, font=("微软雅黑", 11)).pack(side=tk.LEFT, padx=5)
        tk.Checkbutton(hobby_frame, text="编程", variable=self.var_hobby3, font=("微软雅黑", 11)).pack(side=tk.LEFT, padx=5)
        hobby_frame.grid(row=6, column=1, sticky=tk.W, pady=8)
        
        btn_frame = tk.Frame(frame)
        tk.Button(btn_frame, text="提交", command=self.submit, font=("微软雅黑", 11), 
                  bg="#5cb85c", fg="white", width=10).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="取消", command=self.top.destroy, font=("微软雅黑", 11), 
                  bg="#d9534f", fg="white", width=10).pack(side=tk.LEFT, padx=10)
        btn_frame.grid(row=7, column=0, columnspan=3, pady=20)
        
        frame.pack()

        if self.edit_data:
            self.entry_sid.insert(0, self.edit_data[0])
            self.entry_sid.config(state=tk.DISABLED)
            self.entry_name.insert(0, self.edit_data[1])
            self.var_gender.set(self.edit_data[2])
            self.entry_age.insert(0, self.edit_data[3])
            self.entry_class.insert(0, self.edit_data[4])
            self.entry_phone.insert(0, self.edit_data[5])
            hobbies = self.edit_data[6].split("、")
            self.var_hobby1.set("运动" in hobbies)
            self.var_hobby2.set("阅读" in hobbies)
            self.var_hobby3.set("编程" in hobbies)

    def submit(self):
        sid = self.entry_sid.get().strip()
        name = self.entry_name.get().strip()
        gender = self.var_gender.get()
        age = self.entry_age.get().strip()
        cls = self.entry_class.get().strip()
        phone = self.entry_phone.get().strip()
        
        hobbies = []
        if self.var_hobby1.get(): hobbies.append("运动")
        if self.var_hobby2.get(): hobbies.append("阅读")
        if self.var_hobby3.get(): hobbies.append("编程")
        hobby_text = "、".join(hobbies) if hobbies else "无"

        if not is_valid_student_id(sid):
            messagebox.showwarning("输入错误", "学号必须是8位数字！")
            self.entry_sid.focus()
            return
        if not name:
            messagebox.showwarning("输入错误", "姓名不能为空！")
            self.entry_name.focus()
            return
        if not age.isdigit() or int(age) < 0 or int(age) > 100:
            messagebox.showwarning("输入错误", "年龄必须是0-100的数字！")
            self.entry_age.focus()
            return
        if not cls:
            messagebox.showwarning("输入错误", "班级不能为空！")
            self.entry_class.focus()
            return
        if phone and not is_valid_phone(phone):
            messagebox.showwarning("输入错误", "手机号格式错误！")
            self.entry_phone.focus()
            return

        student_data = (sid, name, gender, age, cls, phone, hobby_text)
        self.callback(student_data, is_edit=bool(self.edit_data))
        self.top.destroy()

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("学生管理系统 v1.0")
        self.master.geometry("1000x600")
        
        self.student_data = [
            ("20240001", "张三", "男", "20", "计科2401", "13800138000", "运动、编程"),
            ("20240002", "李四", "女", "19", "计科2401", "13900139000", "阅读"),
            ("20240003", "王五", "男", "21", "软工2402", "13700137000", "运动、阅读")
        ]
        self.init_ui()

    def init_ui(self):
        top_frame = tk.Frame(self.master, pady=10)
        tk.Button(top_frame, text="新增学生", command=self.add_student, font=("微软雅黑", 11), 
                  bg="#5bc0de", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="编辑选中", command=self.edit_student, font=("微软雅黑", 11), 
                  bg="#f0ad4e", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="删除选中", command=self.del_student, font=("微软雅黑", 11), 
                  bg="#d9534f", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="清空数据", command=self.clear_student, font=("微软雅黑", 11), 
                  bg="#777777", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="导出CSV", command=self.export_csv, font=("微软雅黑", 11), 
                  bg="#5cb85c", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="导入CSV", command=self.import_csv, font=("微软雅黑", 11), 
                  bg="#337ab7", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        top_frame.pack(fill=tk.X, padx=20)

        filter_frame = tk.Frame(self.master, pady=10)
        tk.Label(filter_frame, text="筛选：", font=("微软雅黑", 11)).pack(side=tk.LEFT, padx=5)
        self.entry_filter = tk.Entry(filter_frame, font=("微软雅黑", 11), width=30)
        self.entry_filter.pack(side=tk.LEFT, padx=5)
        tk.Button(filter_frame, text="按姓名/学号/班级筛选", command=self.filter_student, font=("微软雅黑", 11), 
                  width=18).pack(side=tk.LEFT, padx=5)
        tk.Button(filter_frame, text="重置筛选", command=self.reset_filter, font=("微软雅黑", 11), 
                  width=10).pack(side=tk.LEFT, padx=5)
        filter_frame.pack(fill=tk.X, padx=20)

        table_frame = tk.Frame(self.master)
        columns = ("sid", "name", "gender", "age", "class", "phone", "hobby")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        self.tree.heading("sid", text="学号")
        self.tree.heading("name", text="姓名")
        self.tree.heading("gender", text="性别")
        self.tree.heading("age", text="年龄")
        self.tree.heading("class", text="班级")
        self.tree.heading("phone", text="手机号")
        self.tree.heading("hobby", text="爱好")
        self.tree.column("sid", width=100, anchor=tk.CENTER)
        self.tree.column("name", width=80, anchor=tk.CENTER)
        self.tree.column("gender", width=60, anchor=tk.CENTER)
        self.tree.column("age", width=60, anchor=tk.CENTER)
        self.tree.column("class", width=100, anchor=tk.CENTER)
        self.tree.column("phone", width=120, anchor=tk.CENTER)
        self.tree.column("hobby", width=150, anchor=tk.CENTER)
        
        scroll_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll_y.set)
        self.tree.pack(side=tk.LEFT)
        scroll_y.pack(side=tk.LEFT, fill=tk.Y)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.stat_var = tk.StringVar(value="")
        stat_frame = tk.Frame(self.master, pady=10)
        tk.Label(stat_frame, textvariable=self.stat_var, font=("微软雅黑", 11, "bold"), fg="#d9534f").pack()
        stat_frame.pack(fill=tk.X, padx=20)

        self.refresh_table()
        self.update_stat()

    def refresh_table(self, data=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
        display_data = data if data else self.student_data
        for row in display_data:
            self.tree.insert("", tk.END, values=row)

    def update_stat(self):
        total = len(self.student_data)
        if total == 0:
            self.stat_var.set(f"统计：总人数 0 | 男生 0 | 女生 0 | 班级数 0")
            return
        male = len([row for row in self.student_data if row[2] == "男"])
        female = total - male
        classes = set([row[4] for row in self.student_data])
        self.stat_var.set(f"统计：总人数 {total} | 男生 {male} | 女生 {female} | 班级数 {len(classes)}")

    def add_student(self):
        def callback(student_data, is_edit):
            for row in self.student_data:
                if row[0] == student_data[0]:
                    messagebox.showwarning("错误", "学号已存在！")
                    return
            self.student_data.append(student_data)
            self.refresh_table()
            self.update_stat()
            messagebox.showinfo("成功", "学生信息新增成功！")
        StudentFormWindow(self.master, callback)

    def edit_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("提示", "请先选中要编辑的学生！")
            return
        row_data = self.tree.item(selected[0])["values"]
        def callback(student_data, is_edit):
            for i, row in enumerate(self.student_data):
                if row[0] == student_data[0]:
                    self.student_data[i] = student_data
                    break
            self.refresh_table()
            self.update_stat()
            messagebox.showinfo("成功", "学生信息编辑成功！")
        StudentFormWindow(self.master, callback, edit_data=row_data)

    def del_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("提示", "请先选中要删除的学生！")
            return
        if not messagebox.askyesno("确认", "确定要删除选中的学生吗？"):
            return
        selected_sids = [self.tree.item(item)["values"][0] for item in selected]

        self.student_data = [row for row in self.student_data if int(row[0]) not in selected_sids]

        self.refresh_table()
        self.update_stat()
        messagebox.showinfo("成功", "学生信息删除成功！")

    def clear_student(self):
        if not self.student_data:
            messagebox.showinfo("提示", "暂无学生数据可清空！")
            return
        if not messagebox.askyesno("确认", "确定要清空所有学生数据吗？此操作不可恢复！"):
            return
        self.student_data = []
        self.refresh_table()
        self.update_stat()
        messagebox.showinfo("成功", "所有学生数据已清空！")

    def filter_student(self):
        keyword = self.entry_filter.get().strip().lower()
        if not keyword:
            self.refresh_table()
            return
        filtered = [row for row in self.student_data if 
                    keyword in row[0].lower() or 
                    keyword in row[1].lower() or 
                    keyword in row[4].lower()]
        self.refresh_table(filtered)
        messagebox.showinfo("筛选结果", f"共找到 {len(filtered)} 条匹配数据")

    def reset_filter(self):
        self.entry_filter.delete(0, tk.END)
        self.refresh_table()

    def export_csv(self):
        if not self.student_data:
            messagebox.showwarning("提示", "暂无数据可导出！")
            return
        filename = simpledialog.askstring("导出CSV", "请输入文件名（无需.csv）：", initialvalue=f"学生数据_{datetime.now().strftime('%Y%m%d')}")
        if not filename:
            return
        filename += ".csv"
        try:
            with open(filename, "w", encoding="utf-8-sig", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["学号", "姓名", "性别", "年龄", "班级", "手机号", "爱好"])
                writer.writerows(self.student_data)
            messagebox.showinfo("成功", f"数据已导出到：{filename}")
        except Exception as e:
            messagebox.showerror("失败", f"导出失败：{str(e)}")

    def import_csv(self):
        filename = simpledialog.askstring("导入CSV", "请输入CSV文件名（含路径）：")
        if not filename:
            return
        try:
            with open(filename, "r", encoding="utf-8-sig") as f:
                reader = csv.reader(f)
                next(reader)
                imported = []
                for row in reader:
                    if len(row) != 7 or not is_valid_student_id(row[0]):
                        continue
                    imported.append(tuple(row))
                existing_sids = [row[0] for row in self.student_data]
                new_data = [row for row in imported if row[0] not in existing_sids]
                self.student_data.extend(new_data)
                self.refresh_table()
                self.update_stat()
            messagebox.showinfo("成功", f"共导入 {len(new_data)} 条新数据（{len(imported)-len(new_data)} 条重复数据已跳过）")
        except FileNotFoundError:
            messagebox.showerror("失败", "文件不存在！")
        except Exception as e:
            messagebox.showerror("失败", f"导入失败：{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()