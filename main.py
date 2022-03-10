#!/user/bin/python
# -*- coding:utf-8 -*-
# 作者：realityerror
# 创建：2022-03-10
# 更新：2022-03-10
# 用意：建立服务器后端,为前端提供一些数据

#数据库(简单表)初始化
from typing import Tuple
from database import database

#引用一些变量
from init import *

#调用thinker图形化界面
import tkinter as tk
from tkinter import *



#按钮的回调函数
def btn1():
    print ("click me!")

#主程序运行
if __name__ == '__main__':
#初始化窗口
    window =tk.Tk()               #创建主窗口
    # 给主窗口起一个名字，也就是窗口的名字
    window.title('ESP32后端服务系统')
    # 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
    window.geometry('600x400')
    #开启主循环，让窗口处于显示状态
    window.iconbitmap('../ESP32webserve/static/picture/robot.ico')

#初始化按钮控件
# 设置回调函数

# 使用按钮控件调用函数
    btn1 = tk.Button(window, text="后端初始化", command= btn1,).place(x=10,y=10)




#初始化文本框控件
# 创建一个文本控件
# width 一行可见的字符数；height 显示的行数
    text = Text(window,  undo=True, autoseparators=False)
# 适用 pack(fill=X) 可以设置文本域的填充模式。比如 X表示沿水平方向填充，Y表示沿垂直方向填充，BOTH表示沿水平、垂直方向填充
    text.place(x=40,y=40,width=200,height=100)
# INSERT 光标处插入；END 末尾处插入
    text.insert(INSERT, '测试文本')


#运行窗口程序
    window.mainloop()


#运行数据获取程序
    while True:
        pass