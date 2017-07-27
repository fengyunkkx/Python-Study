def myFirstFuncation(): #第一个函数
	print("这是我创建的第一个函数！")
	print("我表示非常的激动！")
	print("我要感谢CCTV！感谢Python！")
	
def mySecondFuncation(name): #参数
	print(name + "是帅哥！")

def add(num1,num2): #返回值
	return num1 +num2
	
def exchangeRate(dollar): #函数文档
	"""
	美元->人民币
	汇率暂定为 6.5
	"""
	return dollar * 6.5
	
def test (* params, extra): #收集参数
	print("收集参数是：",params)
	print("位置参数是：",extra)
	
def test (* params, extra="8"): #收集参数加上默认参数
	print("收集参数是：",params)
	print("位置参数是：",extra)
	
def test (* params): #收集参数的解包
	print("有 %d 个参数" % len(params))
	print("第二个参数是：",params[1])
	
