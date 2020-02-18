# -*- coding: utf-8 -*-
# Author      : surfer
# time        : 2020/1/14 21:51
# name        : re.py
# projec_tname: python
# IDE         : PyCharm

import re

pattern = re.compile(r'\d{4}')
a='666-09'
m = pattern.match(a)
print m
