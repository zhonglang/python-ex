# -*- coding:utf-8 -*-
import requests

# 1、get请求，传参params={},需要请求头headers={}
# r = requests.get('https://www.douban.com/',params={'a':100,'b':200})
# print r
# print r.url
# print r.status_code
# print r.encoding
# # print r.text  r.text 返回headers中的编码解析的结果，可以通过r.encoding = 'gbk'来变更解码方式
# # print r.content  r.content返回二进制结果
# # r.json()返回JSON格式，可能抛出异常
#
# # 2、post请求,传入data参数作为post的参数data={}
# r = requests.post('https://www.baidu.com',data={'a':100,'b':200})
#
import json

url = 'http://paas.bktest.com/api/c/compapi/v2/cc/search_host/'
data = {
    'bk_app_code': 'general-check',
    'bk_app_secret': 'c91d8cbe-2fd1-4eac-bab0-3e8885c96e6c',
    'bk_username': 'admin',
    'bk_biz_id': 2
    # "condition": [{
    #     "bk_obj_id": "host",
    #     "fields": [],
    #     "condition": [
    #         {
    #             "field": "bk_host_innerip",
    #             "operator": "$eq",
    #             "value": '192.168.103.29'
    #         }
    #     ]
    # }]

}
r = requests.post(url, data=data)
# print r.content
for i in json.loads(r.content)['data']['info']:
    if i['host']['bk_host_innerip'] == '192.168.103.29':
        print i['host']
        print i['host']['bk_cloud_id']

# data1 = {
#     'bk_app_code': 'general-check',
#     'bk_app_secret': 'c91d8cbe-2fd1-4eac-bab0-3e8885c96e6c',
#     'bk_username': 'admin',
#     "bk_supplier_account": "0",
#     # "bk_obj_id": "plat",
#     # "bk_inst_id": 2,
#     # "bk_cloud_name": "test"
#     "bk_host_id": "39",
#     "data": {
#         "host_vip": "test"
#     }
# }
# url1 = 'http://paas.bktest.com/api/c/compapi/v2/cc/update_host/'
# r1 = requests.post(url1, data=data1)
# print r1.content
