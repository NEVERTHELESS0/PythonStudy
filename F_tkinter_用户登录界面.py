#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter
import tkinter.messagebox
# 创建应用窗口
root = tkinter.Tk()
root.title('用户登录程序')
varName = tkinter.StringVar()
varName.set('')
varPwd = tkinter.StringVar()
varPwd.set('')
# 创建用户名标签,讲用户名标签放到窗口上
labelName = tkinter.Label(root, text='用户名:', justify=tkinter.RIGHT, width=80)
labelName.place(x=10, y=5, width=80, height=20)

# 创建用户名文本框,将用户名文本框放到窗口上
entryName = tkinter.Entry(root, width=80, textvariable=varName)
entryName.place(x=100, y=5, width=80, height=20)

# 创建密码标签,将用户名标签放到窗口上
labelPwd = tkinter.Label(root, text='密码:', justify=tkinter.RIGHT, width=80)
labelPwd.place(x=10, y=30, width=80, height=20)

# 创建密码文本框,将密码文本框放到窗口上
entryPwd = tkinter.Entry(root, width=80, textvariable=varPwd, show='*')
entryPwd.place(x=100, y=30, width=80, height=20)


# 登记按钮事件处理函数
def login():
    name = entryName.get()
    pwd = entryPwd.get()
    if(name == 'liyang' and pwd == '123456'):
        tkinter.messagebox.showinfo(title='提醒', message='登录成功')

    else:
        tkinter.messagebox.showerror('提醒', message='登录失败')


# 创建按钮组件，同时设置按钮事件处理函数
buttonOk = tkinter.Button(root, text='确认', command=login)
buttonOk.place(x=30, y=70, width=50, height=20)


# 取消按钮事件处理函数
def cancel():
    varName.set('')
    varPwd.set('')


# 创建按钮组件，同时设置按钮事件处理函数
buttonCancel = tkinter.Button(root, text='取消', command=cancel)
buttonCancel.place(x=90, y=70, width=50, height=20)
root.mainloop()