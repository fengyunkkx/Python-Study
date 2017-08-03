文件系统 OS

import os

os.getcwd() #获取目录

os.chdir(path) #改变工作目录

os.listdir(path='.') #列举当前目录文件

os.mkdir("test") #创建文件夹

os.makedirs(r". \a\b\c") #创建多层目录

os.remove(path) rmdir(path) removedirs(path) #删除文件、删除文件夹、删除多层目录

os.rename(old,new) #重命名文件或文件夹

os.system(command) #调用系统工具

os.walk(top) 
