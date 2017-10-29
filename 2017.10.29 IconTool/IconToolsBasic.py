# -*- coding: UTF-8 -*-


## 导入 os
import os

'''
总体思路：
1. 检测当前目录下是否有 .ico 文件。
2. 获取 .ico 文件的文件名。
3. 新建一个 desktop.ini 文件，设为隐藏。
4. 将文件夹设置为只读。
'''


## 1. 检测当前目录下是否有 .ico 文件。
def first_step():
	print ('1. 检测当前目录下是否有 .ico 文件')
	filepath = os.getcwd()
	print ('当前路径:' + filepath)
	path = os.chdir(filepath)
	
	Const_Image_Format = [".ico"] ## 需要寻找的文件格式

	class FileFilt:
		fileList = [""]
		counter = 0  ## counter 计数
		def __init__(self): ## 初始化对象
			pass
		def FindFile(self,dirr,filtrate = 1):
			global Const_Image_Format   ## 调用全局变量 Const_Image_Format
			for s in os.listdir(dirr):  ## 利用 listdir 列举文件名
				newDir = os.path.join(dirr,s)
				if os.path.isfile(newDir):
					if filtrate:
						if newDir and(os.path.splitext(newDir)[1] in Const_Image_Format): ## 利用 splitext 分离文件名与扩展名，与 Const_Image_Format 做匹配
							self.fileList.append(newDir)
							self.counter+=1

							os.rename(newDir,"iconfile.ico")
							print ('检测完毕！\n')
	
## 2. 获取 .ico 文件的文件名。
def second_step():
	print ('2. 正在获取 .ico 文件的文件名')

	
	print ('获取完毕！\n')
		
		
## 3. 新建一个 desktop.ini 文件，设为隐藏。
def third_step():
	print ('3. 正在新建一个 desktop.ini 文件')
	
	## 将文件夹图标设置为同文件夹下的 iconfile.ico 图标（覆盖原内容）
	
	## 配置信息
	iniline1 = "[.ShellClassInfo]"
	iniline2 = "IconResource=iconfile.ico,0"
	iniline = iniline1 + "\n"+ iniline2

	## 为 desktop.ini 写入配置
	inifile = open('desktop.ini','w')
	inifile.write(iniline)
	inifile.close()

	## 将 desktop.ini 设为隐藏
	## To-Do
	
	print ('新建完毕！\n')


## 4. 将文件夹设置为只读。
def fourth_step():
	print ('4. 正在将文件夹设置为只读')

	
	print ('设置完成！\n')



## 定义 main

def main():
	first_step()
	second_step()
	third_step()
	fourth_step()

## 开始执行	

main()

## 结束任务
