# -*- coding: utf-8 -*-
# 闭包：在函数里面又定义了函数，并且内函数用到了外边函数的变量，那么将整个整体称为闭包
def test(number):
    def test_in(number_in):
        print('in test_in函数,number_in is %d' %number_in)
        return number_in + number
    return test_in


fun = test(10)
print(fun(100))
