import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox


# 定义菜单功能函数
# 1.新建文件
def newf():
    if tk.messagebox.askquestion('提示', '是否保存文件？') == 'yes':
        savefile()
    else:
        text.delete(1.0, tk.END)


# 2.打开文件
def openfile():
    if tk.messagebox.askquestion('提示', '是否保存文件？') == 'yes':
        savefile()
    else:
        text.delete(1.0, tk.END)
        filename = tk.filedialog.askopenfilename(title='File', filetypes=[('文本文档', '*.txt'), ('其他文件', '*.*')])
        print(filename)
        if not filename:
            return
        txt = open(filename).read()
        text.insert("1.0", txt)
        root.title("%s-记事本" % filename.split('/')[-1])


# 3.保存文件
def savefile():
    filename = tk.filedialog.asksaveasfilename(title='另存为', initialfile='未命名.txt', filetypes=[('文本文档', '*.txt')])
    print(filename)
    if not filename:
        return
    fn = open(filename, 'w')
    fn.write(text.get(1.0, tk.END))


# 4.退出
def fquit():
    global root
    if tk.messagebox.askquestion('提示', '是否保存文件？') == 'yes':
        savefile()
        root.destroy()
    else:
        root.destroy()


# 5.全选
def select_all():
    text.tag_add(tk.SEL, 1.0, tk.END)
    text.see(tk.INSERT)
    text.focus()


# 6.复制
def copy():
    textc = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    text.clipboard_clear()
    text.clipboard_append(textc)


# 7.粘贴
def paste():
    try:
        textp = text.selection_get(selection='CLIPBOARD')
        text.insert(tk.INSERT, textp)
        text.clipboard_clear()
    except tk.TclError:
        pass


# 8.关于记事本
def about():
    tk.messagebox.showinfo(title="欢迎使用吴team记事本", message="作者吴team\n版本:1.0")


# 9.版权信息
def copyr():
    tk.messagebox.showinfo(title="欢迎使用吴team记事本", message="© 2023 Wu_team。保留所有权利。\n该项目已托管至Github平台，名称：wu_team_notepad")


root = tk.Tk()
root.title("无标题-记事本")
root.geometry("600x400+100+100")
menubar = tk.Menu(root)
fmenu = tk.Menu(menubar)
fmenu.add_command(label="新建", accelerator='Ctrl+N', command=newf)
fmenu.add_command(label="打开", accelerator='Ctrl+O', command=openfile)
fmenu.add_command(label="保存", accelerator='Ctrl+S', command=savefile)
fmenu.add_separator()
fmenu.add_command(label="退出", command=fquit)
vmenu = tk.Menu(menubar)
vmenu.add_command(label="全选", accelerator='Ctrl+A', command=select_all)
vmenu.add_command(label="复制", accelerator='Ctrl+C', command=copy)
vmenu.add_command(label="粘贴", accelerator='Ctrl+V', command=paste)
amenu = tk.Menu(menubar)
amenu.add_command(label="关于记事本", command=about)
amenu.add_command(label="版权信息", command=copyr)
menubar.add_cascade(label='文件', menu=fmenu)
menubar.add_cascade(label="编辑", menu=vmenu)
menubar.add_cascade(label="关于", menu=amenu)
root['menu'] = menubar
text = tk.Text()
text.pack(expand=tk.YES, fill=tk.BOTH)
root.mainloop()
