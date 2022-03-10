#!/user/bin/python
# -*- coding:utf-8 -*-
# 作者：realityerror
# 创建：2022-03-10
# 更新：2022-03-10
# 用意：初始化一些变量方便引用






#初始化一些数据库位置
database_user = "../ESP32webserve/database/database_user.xlsx"
database_ro = "../ESP32webserve/database/database_ro.xlsx"


#初始化运行日志库
IP_use = "../ESP32webserve/database/IP.txt"

#注意上面的内容跟webserve里面有一些不一样



f = open(IP_use,"r")   #设置文件对象
IP = f.read()     #将txt文件的所有内容读入到字符串str中
f.close()   #将文件关闭

