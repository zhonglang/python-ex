# -*- coding: utf-8 -*-
# Author      : surfer
# time        : 2020/3/2 19:09
# name        : wxchat.py
# projec_tname: python
# IDE         : PyCharm
# with用法
class Sample:
    def __enter__(self):
        print "In __enter__()"
        return "Foo"

    def __exit__(self, type, value, trace):
        print "In __exit__()"
        print type
        print value
        print trace


def get_sample():
    return Sample()

#　sample接收Sample()中enter函数的返回值
with get_sample() as sample:
    print "sample:", sample
