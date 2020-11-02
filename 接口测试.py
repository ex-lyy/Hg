# -*- coding:utf-8 -*-
# 文件名称：Lyy-接口测试
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/10/30 14:40

'''
接口：API

http://jmp.joowing.com/api/ris/sessions.json?session%5Blogin%5D=chong.chen&session%5Bpassword%5D=ex19950816

开发：前端（H5，javascript，ajax）、后端（开发）
    后端接受前端的请求，返回给前端数据
	前端接受后端的返回数据，处理数据
	后端数据在前端展示实际是由浏览器完成，浏览器做到了渲染的功能

	所以浏览器到前端到后台，实际上设计很多的数据交互。
	get：把请求的参数直接放在链接后面，用？和&链接 不安全的
	post：

	cookie：保存用户信息，浏览器的功能（是一个保存在本地电脑的文件，里面写的是用户的信息，文件有一个有效期） 也不是安全的，可以在本地找到，也可以在请求的时候被抓到
	session：和cookie差不多，但是session是放在服务器的。请求的时候浏览器把session的ID传给服务器，服务器验证这个ID和放在服务器的session是否匹配，匹配即允许

'''
import selenium
import requests
import json

# request_url = 'http://jmp.joowing.com/api/ris/sessions.json?session%5Blogin%5D=chong.chen&session%5Bpassword%5D=ex19950816'
# res = requests.post(request_url)
# print(res) #打印请求信息
# print(res.status_code) #打印请求状态
# print(res.content) #打印请求数据（二进制文本格式）
# print(res.json()) #打印请求数据（json数据格式）
# print(res.cookies)#打印cookies
# for i in res.cookies:
#     print(i)


headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.11 Safari/537.36",
    "Cookie": "UM_distinctid=1756e5b41ce4c0-00cecff9e782a-c791930-1fa400-1756e5b41cfc90; retailer=%7B%22id%22%3A58%2C%22code%22%3A%22ygyj%22%2C%22name%22%3A%22%E9%98%B3%E5%85%89%E7%9B%8A%E4%BD%B3%22%2C%22businesses%22%3A%5B%22payin%22%2C%22consign%22%5D%7D; joowing-session-id=522677d7e77cf279be6550375c221f6f; login=chong.chen; joowing-staff-jwt=eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiY2hvbmcuY2hlbiIsImVtYWlsIjoiY2hvbmcuY2hlbkBqb293aW5nLmNvbSIsInR5cGUiOiJqb293aW5nLXN0YWZmIiwiZXhwIjoxNjA0MDg0MzA0fQ.W5QM41badCpDlDTG-YtGDx0MhnbYiWLNhId-tdizdW0",
    'Content-Type': 'application/json;charset=UTF-8'

}

data =json.dumps({"org_code" : "lebaby", "phone" : "17633705244"})
request_url_coupon = 'http://jmp.joowing.com/api/ris/spi/lebaby/members/__query'

res_2 = requests.post(request_url_coupon,headers=headers,data=data)
print(res_2)
date = res_2.json()
print(date)


# for i in date:
#     print("券名称：",i['coupon_definition']['name'],end='')
#     print("券号：",i['serial_no'],end='')
#     print("会员号：",i['member_no'],end='')
#     print("使用情况：",i['record_type'],end='')
#     print("code：",i['code'],end='')
#     print("开始时间：",i['begin_date'],end='')
#     print("结束时间：",i['end_date'])



import requests

# 获取NB登录的请求头
class get_nb_cookies():
    def __init__(self, org_code, password):
        self.org_code = org_code
        self.password = password

    def get_cookies(self):
        login_url = r"http://nb3.joowing.com/nebula/v3/session?session%%5Blogin%%5D=js1@%s.com&session%%5Bpassword%%5D=%s" % (
            self.org_code, self.password)

        login_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }

        login_result = requests.post(login_url, headers=login_headers)

        request_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            "Cookie": "id5AA=c5/nn1vC8o4vZul8i2zJAg==; Hm_lvt_b4a22b2e0b326c2da73c447b951236d6746=1539760959; xxzl_deviceid=F 3hTrG /V/iuVTvmXAxCandrfhokre4OxgMOfI7Tgxtvi1aO/IsvAfVCg7v1KEn;"
        }

        request_headers['Cookie'] = ";".join([request_headers['Cookie'], ";".join('='.join(i) for i in login_result.cookies.items())])
        return request_headers