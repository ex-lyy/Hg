# -*- coding:utf-8 -*-
# 文件名称：Hg-lyycc-聚合支付二维码下载
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/11/23 14:38

from TestMain import *
import requests
import json

org_code_list = []

org_code = 'subujyl'
password = 'js1109'

headers = get_nb_cookies(org_code, password).get_cookies()
headers['Content-Type'] = 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryRy5649AnBe7tuQba'
headers['Content-Encoding'] = 'gzip, deflate, br'

# request_url = r'http://nb3.joowing.com/api/unipay/subujyl/qr_code/queryList.jsonc'
# data = {'page[index]': '1', 'page[size]': '20', 'sort[update_at]': 'desc'}
request_type = 'post'


# request_data = request_nb_api(request_url, headers,data,request_type).request_reponse_json()
#
# for i in request_data:
#     print(request_data)

headers['Cookies'] = 'Cookie: _newbee_session=4a58e80d3972fa1d02ba3f270db58592; joowing-session-id=4a58e80d3972fa1d02ba3f270db58592; serial=%7B%22code%22%3A%22RUIBUEN_1%22%2C%22name%22%3A%22%E7%91%9E%E5%93%BA%E6%81%A9%E6%9C%89%E6%9C%BA%22%7D; login=js1%40subujyl.com; JSESSIONID=node01g36j9duux15n1cd95v4r0eg381728.node0; retailer-staff-jwt=eyJhbGciOiJIUzI1NiJ9.eyJpZCI6NDA4NzAsIm5hbWUiOiJqczFAc3VidWp5bC5jb20iLCJuaWNrX25hbWUiOiLmioDmnK8t6IuP54ix5am06YeR5pGH56-uIiwibm8iOiJKVzAwMSIsInBob25lIjoiMTczNjAyNTQ1MTMiLCJ0eXBlIjoiam9vd2luZy1zdGFmZiIsIm9yZ19pZCI6MTA1LCJvcmdfY29kZSI6InN1YnVqeWwiLCJyZXRhaWxlcl9pZCI6MTA1LCJyZXRhaWxlcl9jb2RlIjoic3VidWp5bCIsImV4cCI6MTYwNjIwMDA0OX0.EgzmsQ-npbXVhkLlzlGd4ulyTZ71svHvLEgcbWqYgrk'

files={
  'file':('libmsc.zip',open(r'C:\Users\LyyCc\Desktop\a_1600655403420.png','rb'))
 }

request_url=r'https://content.joowing.com/content_node/contents/write.json'
request_data =requests.post(url = request_url,files=files)
print(request_data)