# -*- coding: utf-8 -*-
# Author      : surfer
# time        : 2019/4/28 11:30
# name        : work.py
# projec_tname: python
# IDE         : PyCharm


# 列表中的字典去重
def list_dict_duplicate_removal():
    data_list = [{"a": "123", "b": "321"}, {"a": "123", "b": "31"}, {"b": "321", "a": "123"}]
    run_function = lambda x, y: x if y in x else x + [y]
    return reduce(run_function, [[], ] + data_list)

