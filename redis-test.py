# -*- coding: utf-8 -*-
# Author      : surfer
# time        : 2020/2/27 17:39
# name        : redis.py
# projec_tname: python
# IDE         : PyCharm
from redis import StrictRedis

r = StrictRedis(host='localhost', port=6379, password='1qaz@WSX', decode_responses=True)
r.set('name', 'zzl')
print r.get('value_one')
print r.dbsize()