# 递归版本的求阶乘
def recursion(n):
	if n == 1:
		return 1
	else:
		return n * recursion( n - 1 )
	
number = int(input('请输入一个整数：'))
result = recursion(number)
print("%d的阶乘是：%d" %(number,result))
