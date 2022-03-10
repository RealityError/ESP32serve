#!/user/bin/python
# -*- coding:utf-8 -*-
# 作者：realityerror
# 创建：2022-03-10
# 更新：2022-03-10
# 用意：建立服务器后端,为前端提供一些数据

#数据库(简单表)初始化
from time import time
from typing import Tuple

from numpy import insert
from database import database

#引用一些变量
from init import *

#调用thinker图形化界面
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#获取时间戳
import datetime
def timelog():
    curr_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(curr_time,'%Y-%m-%d %H:%M:%S')
    return time_str


#按钮的回调函数

def btn1():
    print ("click me!")


def btn2():
    print ("click me!")
#主程序运行
if __name__ == '__main__':
#初始化窗口
    root = ttk.Window(themename="darkly")              #创建主窗口
    # 给主窗口起一个名字，也就是窗口的名字
    root.title('ESP32后端服务系统')
    # 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
    root.geometry('600x400')
    #调用图标
    root.iconbitmap('../ESP32webserve/static/picture/robot.ico')


    

#初始化按钮控件
# 设置回调函数

# 使用按钮控件调用函数
    btn1 = ttk.Button(root, text="后端初始化", command= btn1, bootstyle="success-outline").place(x=10,y=10)
    btn2 = ttk.Button(root, text="检测设备连接情况", command= btn2, bootstyle="success-outline").place(x=150,y=10)



#初始化文本框控件
# 创建一个文本控件
# width 一行可见的字符数；height 显示的行数
    text = ttk.Text(root)
# 适用 pack(fill=X) 可以设置文本域的填充模式。比如 X表示沿水平方向填充，Y表示沿垂直方向填充，BOTH表示沿水平、垂直方向填充
    text.place(x=10,y=100,width=580,height=200)
# INSERT 光标处插入；END 末尾处插入
    text.insert(INSERT, timelog()+'\r\n')


#开启主循环，让窗口处于显示状态
    root.mainloop()


#运行数据获取程序
    while True:
        pass