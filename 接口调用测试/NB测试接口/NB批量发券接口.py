# -*- coding:utf-8 -*-
# 文件名称：Lyy-NB批量发券接口
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/11/11 13:46

from TestMain import *
import requests
import json

org_code = 'demo'
password = 'js1109'
api = r'http://nb3.joowing.com/nebula/v3/promotion/coupon_definitions/batch_send_coupons.json?org_code=demo'
request_type = 'post'

data = {
	"option": [{
		"definition_id": 39416,
		"serial_no": "cp_1602493387109570",
		"display_name": "[cp_1602493387109570]100元瑞哺恩有机优惠券",
		"jw_id": ["849f6c50-8090-0138-58a2-36ddb36c8967", "181a8ad0-c55f-0137-1005-02b12a3fc4f6"],
		"expiration_date_type": "by_date",
		"num": 1,
		"expiration_day": 7,
		"begin_date": "2020-11-12",
		"end_date": "2020-11-30"
	}, {
		"definition_id": 39416,
		"serial_no": "cp_1602493387109570",
		"display_name": "[cp_1602493387109570]100元瑞哺恩有机优惠券",
		"jw_id": ["849f6c50-8090-0138-58a2-36ddb36c8967", "181a8ad0-c55f-0137-1005-02b12a3fc4f6"],
		"expiration_date_type": "by_date",
		"num": 1,
		"expiration_day": 7,
		"begin_date": "2020-12-01",
		"end_date": "2020-12-31"
	}, {
		"definition_id": 39416,
		"serial_no": "cp_1602493387109570",
		"display_name": "[cp_1602493387109570]100元瑞哺恩有机优惠券",
		"jw_id": ["849f6c50-8090-0138-58a2-36ddb36c8967", "181a8ad0-c55f-0137-1005-02b12a3fc4f6"],
		"expiration_date_type": "by_date",
		"num": 1,
		"expiration_day": 7,
		"begin_date": "2021-01-01",
		"end_date": "2021-01-31"
	}],
	"description": "商户要求补发"
}


headers = get_nb_cookies(org_code,password).get_cookies()

Content_Type =  "application/json;charset=UTF-8"
Accept = 'application/json, text/plain, */*'
Accept_Encoding = 'gzip, deflate'
Connection = 'keep-alive'



headers['Content-Type']= Content_Type
headers['Accept']= Accept
headers['Accept-Encoding']= Accept_Encoding
headers['Connection']= Connection
headers['Content-Length']= '1022'

print(headers)

data = json.dumps(data)

response = requests.post(url=api, headers= headers, data = data)
print(response.status_code)
