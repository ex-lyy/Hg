# -*- coding:utf-8 -*-
# 文件名称：Lyy-TestMain
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/10/22 11:20
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

# 请求api接口
class request_nb_api():
    def __init__(self,api,headers,data,request_type):
        self.api= api
        self.headers= headers
        self.data= data
        self.request_type= request_type
    # 返回接口状态码
    def request_reponse_code(self):
        if self.request_type == 'get':
            response = requests.get(self.api,headers=self.headers,data=self.data)
            return response.status_code
        elif self.request_type == 'post':
            response = requests.post(self.api,headers=self.headers,data=self.data)
            return response.status_code
        else:
            print("request方式输入有误！")
            return "error"
    # 返回接口json数据
    def request_reponse_json(self):
        if self.request_type == 'get':
            response = requests.get(self.api,headers=self.headers,data=self.data)
            return response.json()
        elif self.request_type == 'post':
            response = requests.post(self.api,headers=self.headers,data=self.data)
            response.json()
        else:
            print("request方式输入有误！")
            return "error"

