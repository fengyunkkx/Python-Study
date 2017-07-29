#GUI演示
from tkinter import *

root = Tk()

def callback():
    print("被调用了")

# 创建一个顶级菜单
menubar = Menu(root)
# 创建一个下拉菜单「文件」
filemenu = Menu(menubar, tearoff = False)
filemenu.add_command(label = "打开",command = callback)
filemenu.add_command(label = "保存",command = callback)
filemenu.add_separator()
filemenu.add_command(label = "退出",command = root.quit)
filemenu.add_command(label = "小本子还是强的呀",command = callback)
menubar.add_cascade(label = "文件",menu = filemenu)

# 显示菜单
root.config(menu = menubar)

def create():
    top = Toplevel()
    top.title("哇，小本子贼强")
    msg = Message(top, text = "本子可以的")
    msg.pack()

Button(root, text="点开惊喜", command = create).pack()

mainloop()
