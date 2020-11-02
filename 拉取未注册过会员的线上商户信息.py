# -*- coding:utf-8 -*-
# 文件名称：Lyy-拉取未注册过会员的线上商户信息
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/11/2 15:22


from main import *

server, dbconfig, cursor = connect_masterDB('ris_production')

retailer_sql = "SELECT * FROM ris_production.global_retailers WHERE profile_id = '1' AND state = 'online';"

cursor.execute(retailer_sql)
res = cursor.fetchall()

org_list = []
name_list = []

for i in res:
    org_list.append(i['code'])
    name_list.append(i['name'])


print(org_list)
print(name_list)

# # 会员不正常的商户：
# unnormal_member_org_list = []
#
# # 订单奖励数量不正常的商户：
# unnormal_prize_org_list = []
#
# # 促销活动奖励数量不正常的商户：
# unnormal_promotion_org_list = []
#
# # 抽奖活动数量不正常的商户：
# unnormal_marketing_org_list = []
#
#
# for org_code in org_list:
#     # 近三个月未注册会员的信息
#     register_state = "SELECT COUNT(1) as member_count FROM ris_production.members WHERE org_code='%s' AND created_at>='2020-08-01';"%org_code
#     cursor.execute(register_state)
#     member_count = cursor.fetchone()
#     if member_count['member_count'] >= 3:
#         print("%s注册会员数量正常"%org_code)
#     else:
#         unnormal_member_org_list.append(org_code)
#
# for org_code in org_list:
#     # 近三个月没有订单奖励活动的信息
#     prize_activity_state = "SELECT COUNT(1) as prize_count FROM pomelo_backend_production.prize_activities WHERE org_code='%s' AND created_at>='2020-08-01';" % org_code
#     cursor.execute(prize_activity_state)
#     prize_count = cursor.fetchone()
#     if prize_count['prize_count'] >= 1:
#         print("%s订单奖励信息正常" % org_code)
#     else:
#         unnormal_prize_org_list.append(org_code)
#
# for org_code in org_list:
#     # 近三个月没有互动活动的信息
#     marketing_state = "SELECT COUNT(1) as marketing_count FROM pomelo_backend_production.marketing_prize_events WHERE org_code='%s' AND created_at>='2020-08-01';" % org_code
#     cursor.execute(marketing_state)
#     marketing_count = cursor.fetchone()
#     if marketing_count['marketing_count'] >= 1:
#         print("%s抽奖活动信息正常" % org_code)
#     else:
#         unnormal_marketing_org_list.append(org_code)
#
#
# for org_code in org_list:
#     # 近三个月没有促销活动的信息
#     pormotion_state = "SELECT COUNT(1) as pormotion_count FROM pomelo_backend_production.promotion_promotions WHERE org_code='%s' AND created_at>='2020-08-01';" % org_code
#     cursor.execute(pormotion_state)
#     pormotion_count = cursor.fetchone()
#     if pormotion_count['pormotion_count'] >= 1:
#         print("%s促销活动数量正常" % org_code)
#     else:
#         unnormal_promotion_org_list.append(org_code)
#
#
# print(org_list)
# print(unnormal_member_org_list)
# print(unnormal_prize_org_list)
# print(unnormal_promotion_org_list)
# print(unnormal_marketing_org_list)


close_sshserver(server, dbconfig, cursor)