# -*- coding=UTF-8 -*- 
#函数变量的作用域.py
def discounts(price,rate): #错误的局部变量
	final_price = price * rate
	return final_price

old_price = float(input("请输入原价："))
rate = float(input("请输入折扣率："))
new_price = discounts(old_price,rate)
print("打折后的价格是：", new_price)
print("这里试图打印局部变量 final_price 的值；",final_price)
