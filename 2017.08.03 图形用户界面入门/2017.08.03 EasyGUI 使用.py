import easygui as g
import sys

while 1:
        g.msgbox("嘿！欢迎来到第一个有图形界面的游戏！")
        msg = "请问你希望在这里学到什么呢？"
        title = "第一个互动游戏"
        choices = ["学习 Python","学习 C","学习 C#","学习 Java"]
        choice = g.choicebox(msg,title,choices)
        # note that we convert choice to string, in case
        # the user cancelled the choice, and we got none
        g.msgbox("你的选择是："+str(choice),"结果")
        msg = "你希望重新开始小游戏吗？"
        title = "请选择"
        if g.ccbox(msg, title): # show a Continue/Cancel dialog
            pass # user chose Continue
        else:
            sys.exit(0) # user chose Cancel
