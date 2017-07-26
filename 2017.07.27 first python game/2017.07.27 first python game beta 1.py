""" --- 第一个小游戏 --- """
""" 改进版 """
import random

secret = random.randint(1,10)
time = 1
temp = input("来猜猜看我在想哪个数字？有三次机会~\n")
guess = int (temp)

while guess != secret and time <= 3:
	temp = input("你猜错啦，重新输入吧：\n")
	guess = int(temp)
	time += 1
	
	if guess == secret :
		print("居然被你猜对了？")
		print("不过猜对了也没有奖励的哈哈哈！")
	else:
		if guess > secret:
			print("往小了猜！")
		else:
			print("往大了猜！")

print("游戏结束→ →")
