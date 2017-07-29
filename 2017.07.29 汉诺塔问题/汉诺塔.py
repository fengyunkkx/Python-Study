# 利用递归 解决汉诺塔问题
def hanoi(n,x,y,z):
    if n == 1:
        print(x,'-->',z) #如果只有一层，直接从 x 移动到 z 上
    else:
        hanoi(n-1,x,z,y) #将前 n-1 个盘子从 x 移动到 y 上
        print(x,'-->',y) #将最下面的第 64 个盘子从 x 移动到 z 上
        hanoi(n-1,y,x,z) #将 y 上的 63个盘子移动到 z 上
n = int(input('请输入汉诺塔的层数：'))
hanoi(n,'X','Y','Z')
