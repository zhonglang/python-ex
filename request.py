# -*- coding:utf-8 -*-
import requests
# 1、get请求，传参params={},需要请求头headers={}
r = requests.get('https://www.douban.com/',params={'a':100,'b':200})
print r
print r.url
print r.status_code
print r.encoding
# print r.text  r.text 返回headers中的编码解析的结果，可以通过r.encoding = 'gbk'来变更解码方式
# print r.content  r.content返回二进制结果
# r.json()返回JSON格式，可能抛出异常

# 2、post请求,传入data参数作为post的参数data={}
r = requests.post('https://www.baidu.com',data={'a':100,'b':200})


