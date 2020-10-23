# -*- coding:utf-8 -*-
# 文件名称：Lyy-实现Nb系统登录
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/10/21 18:09

import requests
org_code = 'wanpf'
password = 'js0909'

url = r"http://nb3.joowing.com/nebula/v3/session?session%%5Blogin%%5D=js1@%s.com&session%%5Bpassword%%5D=%s"%(org_code,password)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
headers_two = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Cookie": "id5AA=c5/nn1vC8o4vZul8i2zJAg==; Hm_lvt_b4a22b2e0b326c2da73c447b951236d6746=1539760959; xxzl_deviceid=F 3hTrG /V/iuVTvmXAxCandrfhokre4OxgMOfI7Tgxtvi1aO/IsvAfVCg7v1KEn;"
}

result = requests.post(url,headers=headers)


headers_two['Cookie'] =";".join([headers_two['Cookie'],";".join('='.join(i) for i in result.cookies.items())])


import requests
import time

time_str = str(time.time())[:13]

url_rel = r'http://nb3.joowing.com/promotion/promotion_item_templates/query_template.json?_search=false&nd=%s&rows=100&page=1&sidx=&sord=asc' % time_str

result_rel = requests.get(url_rel,headers=headers_two)
print(result_rel.json())