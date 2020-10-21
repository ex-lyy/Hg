# -*- coding:utf-8 -*-
# 文件名称：Lyy-20201021001
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/10/21 15:20

# 检查促销模板是否配置

import requests
import time

time_str = str(time.time())

url = r'http://nb3.joowing.com/promotion/promotion_item_templates/query_template.json?_search=false&nd=%s&rows=100&page=1&sidx=&sord=asc' % time_str

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Cookie": "Hm_lvt_0c2e41563784bcc9e3dabc630b67ef35=1598250593; _ga=GA1.2.1246383103.1598250597; _newbee_session=6129573449df3a20949225201461085d; joowing-session-id=6129573449df3a20949225201461085d; retailer-staff-jwt=eyJhbGciOiJIUzI1NiJ9.eyJpZCI6NTQ1OTksIm5hbWUiOiJqczFAandiYWJ5LmNvbSIsIm5pY2tfbmFtZSI6IuaKgOacrzHigJRqd2JhYnkiLCJubyI6IkpXMDAxIiwicGhvbmUiOiIxMTExMTExMTExMSIsInR5cGUiOiJqb293aW5nLXN0YWZmIiwib3JnX2lkIjo1Miwib3JnX2NvZGUiOiJqd2JhYnkiLCJyZXRhaWxlcl9pZCI6NTIsInJldGFpbGVyX2NvZGUiOiJqd2JhYnkiLCJleHAiOjE2MDMzNTExOTR9.wYMcICjJAT5Bg3Tx4Yqkf_PS3bLS07jy4PnEx_SNOIU; login=js1%40jwbaby.com; serial=%7B%22code%22%3A%22RUIBUEN_1%22%2C%22name%22%3A%22%E7%91%9E%E5%93%BA%E6%81%A9%E6%9C%89%E6%9C%BA%22%7D",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

result = requests.get(url, headers=headers)
template_lits = result.json()['rows']

template_name_list = []
template_code_list = []

for template in template_lits:
    template_name_list.append(template['template_name'])
    template_code_list.append(template['template_code'])

for i in range(len(template_name_list)):
    if template_name_list[i] == "默认":
        print("促销模板名称：",template_name_list[i],"；促销模板code：",template_code_list[i],"。")