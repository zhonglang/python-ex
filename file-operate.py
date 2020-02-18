# -*- coding:utf-8 -*-

# f.read()一次性读取文件所有内容
# f.read(size)每次读取固定字节长度的内容
# f.readline()每次读取一行
# f.readlines()
# with open('D:\\zhu\\abc.txt','r') as fr:
#     # str = f.read(10)
#     str = fr.readlines()
#     for i in str:
#         print i.rstrip()

try:
    fr = open(r'D:\zhu\abc.txt','r')
    fw = open(r'D:\zhu\abc1.txt','w')
    for line in fr.readlines():
        fw.writelines(line)
finally:
    fr.close()
    fw.close()


# write()
# writelines()
with open(r'D:\zhu\abc1.txt','a+') as fw:
    fw.writelines('ccdc')


# r r+ rb rb+
# w w+ wb wb+
# a a+ ab ab+