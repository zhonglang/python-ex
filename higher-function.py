# -*- coding:utf-8 -*-
# 1、 map():接受2个参数，第一个参数为函数，第二个为序列，map将传入序列的每个元素作用于第一个参数中的函数,并把新的list作为结果返回
def f(x):
    return x*x

# reuslt = map(f,range(1,10))
# print(reuslt)


# 2、reduce(),接收2个参数，第一个参数为函数，第二个为序列，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

def f1(x,y):
    return x*y

# result = reduce(f1,range(1,10))
# result = sum(range(1,10))
# print result
# 需求，将[1,3,5,7]生成1357

def f2(x,y):
    return 10*x + y

result = reduce(f2,range(1,8,2))
# print result


# 3、filter(),接受2个参数，第一个参数为函数，第二个为序列，filter将传入序列的每个元素作用于第一个参数中的函数,
# 根据函数返回的结果是True还是False，决定该元素是保留还是去掉
def f3(x):
    return x % 2 ==0

result = filter(f3,range(1,10))
# print result

#  sorted(iterable, cmp=None, key=None, reverse=False)
# 忽略大小写排序
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

# new_list = sorted(['bob', 'about', 'Zoo', 'Credit'], cmp=cmp_ignore_case)
# print new_list

# 例1. 按照元素出现的次数来排序
# seq = [2,4,3,1,2,2,3]
# # 按次数排序
# seq2 = sorted(seq, key=lambda x:seq.count(x))
# print(seq2) # [4, 1, 3, 3, 2, 2, 2]
# # 改进：第一优先按次数，第二优先按值
# seq3 = sorted(seq, key=lambda x:(seq.count(x), x))
# print(seq3) # [1, 4, 3, 3, 2, 2, 2]
# '''
# 原理：
#   先比较元组的第一个值，值小的在前。（注意：False < True）
#   如果相等就比较元组的下一个值，以此类推。
# '''

#例3. 一道面试题：
list1 = [7, -8, 5, 4, 0, -2, -5]
#要求1.正数在前负数在后 2.正数从小到大 3.负数从大到小
list2 = sorted(list1,key=lambda x:(x<0,abs(x)))
print(list2) # [0,4,5,7,-2,-5,-8]

