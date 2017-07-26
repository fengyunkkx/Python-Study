""" --- 第一个小游戏 --- """
temp = input("来猜猜看我在想哪个数字？")
guess = int (temp)
if guess == 8 :
	print("居然被你猜对了？")
	print("猜对了也没有奖励的哈哈哈！")
else:
	print("猜错啦，我想的是8！")
print("游戏结束→ →")