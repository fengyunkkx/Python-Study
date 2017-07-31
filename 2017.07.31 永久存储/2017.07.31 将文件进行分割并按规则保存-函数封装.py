# 将文件进行分割并按照规则保存

def split_file(file_name):
    count = 1
    boy = []
    girl = []
    f = open('record.txt')
    for each_line in f :
        if each_line[:6] '== == ==':
            (role, line_spoken) = each_line.split(':',1))
            if role == '甲':
                boy.append(line_spoken)
            if role == '乙':
                girl.append(line_spoken)
        else:
            save_file(boy,girl,count)
            boy = []
            girl = []
            count += 1
    save_file(boy,girl,count)
    f.close()
split_file('record.txt')
