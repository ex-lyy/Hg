# -*- encoding：utf-8 -*-
# 文件名称：Lyy-查询会员返豆记录
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/10/10 下午 02:52

from 致维网络.joowMain import *
import re
import datetime


org_code = 'aitiantian'
phone = '13655961020'

member_data = find_member_info_by_phone(org_code,phone)
bean_info_data = find_plus_member_bean_list(org_code,member_data['jw_id'])
print("会员姓名：",member_data['name'],"；\t会员卡号：",member_data['member_no'],"；\t会员手机号：",member_data['phone'],"。")
print("当前数量","\t\t之前数量","\t\t总数量","\t\t返豆类型","\t\t订单号","\t\t\t\t返豆组ID","\t\t返豆时间","\t\t当笔商品条码","\t\t当笔商品金额","\t\t当笔商品时间","\t\t返豆比率")

for i in bean_info_data:
    amount = i['amount']
    pre_amount = i['pre_amount']
    post_amount = i['post_amount']
    source_code = i['source_code']
    order_no = re.search("-\S*-",i['uniq_id']).group().replace('-','')
    group_id = re.search("-\d*$",i['uniq_id']).group().replace('-','')
    time_s = eval(i['source_payload'])['time']
    UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
    utcTime = datetime.datetime.strptime(time_s, UTC_FORMAT)
    localtime = utcTime + datetime.timedelta(hours=8)
    print(localtime)
