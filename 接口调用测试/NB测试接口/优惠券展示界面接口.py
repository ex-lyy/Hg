# -*- coding:utf-8 -*-
# 文件名称：Lyy-接口调用测试
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/10/22 11:54

from 接口调用测试.NB测试接口.TestMain import *

org_code = 'wanpf'
password = 'js0909'

api = r'http://nb3.joowing.com/nebula/v3/promotion/coupon_definitions.json?coupon_type=mall&display_in_list=1&org_code=%s&page%%5Bindex%%5D=1&page%%5Bsize%%5D=1000&state=online'%org_code
headers = get_nb_cookies(org_code,password).get_cookies()
print(headers)
data = {}
request_type='get'

coupon_list = request_nb_api(api,headers,data,request_type).request_reponse_json()
for coupon in coupon_list:
    print("{:<40}".format(coupon['serial_no']),coupon['name'])