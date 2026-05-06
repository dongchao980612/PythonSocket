import tkinter as  tk

win = tk.Tk()
win.geometry("250x120+100+100")

win.title("菜单控件")


def open_fun():
    print("打开菜单被点击了！")


def save_fun():
    print("保存菜单被点击了！")


def exit_fun():
    win.quit()


main_menu = tk.Menu(win)
sub_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="文件", menu=sub_menu)

sub_menu.add_command(label="打开", command=open_fun)
sub_menu.add_command(label="保存", command=save_fun)
sub_menu.add_separator()
sub_menu.add_command(label="退出", command=exit_fun)

win.config(menu=main_menu)

win.mainloop()
