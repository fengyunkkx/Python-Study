# 将文件进行分割并按照规则保存

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
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'
        boy_file = open (file_name_boy,'w')
        girl_file = open (file_name_girl,'w')
        boy_file.writelines(boy)
        girl_file.writelines(girl)
        boy = []
        girl = []
        count += 1
file_name_boy = 'boy_' + str(count)+ '.txt'
file_name_girl = 'gile_' + str(count)+ '.txt'
boy_file = open(file_name_boy,'w')
girl_file = open(file_name_girl,'w')
boy_file.writelines(boy)
girl_file.writelines(girl)
boy_file.close()
girl_file.close()
f.close()
