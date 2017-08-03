# try-except 语句
try:
    f = open('我为什么是一个文档.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件打开过程中出错啦TAT\n 错误原因是：' + str(reason))
