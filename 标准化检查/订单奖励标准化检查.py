# -*- coding:utf-8 -*-
# 文件名称：Hg-lyycc-订单奖励标准化检查
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/11/19 18:19

import openpyxl
from Mymain import *

org_code='lebaby'
activity_code= "l002"
if __name__ == '__main__':

    decript = "1.活动名称\n孕期客礼包[prize_activity_15891758749012341]\n2.活动开始时间、订单读取时间\n2020-05-10 ~ 2020-06-10\n3.是否支持导购发奖\n不支持\n4.是否需要顾客自己去领奖不领奖系统晚上统一下发\n第二天统一自动下发\n5.活动范围（门店、区域） 注意限制了门店区域就不要在填写\n全国\n6.活动期间限制次数\n1次\n7.每月、每天限制次数\n1次\n8.参与的品类、商品\nOK\n9.不参与的品类、商品\n10.奖励下发方式（什么场景下下发什么奖励）  兑换券：产康体验3次、婴儿游泳3次\n11.代金券、兑换券奖励参考其检查模板\n12.联系AM线下实际出单测试\n13.规则描述、各奖励描述必填。"

    server, dbconfig, cursor = connect_master_copy_DB('pomelo_backend_production')

    sql = f'''SELECT * FROM pomelo_backend_production.prize_activities WHERE org_code = '{org_code}' AND CODE ='{activity_code}';'''
    cursor.execute(sql)
    data = cursor.fetchone()
    name = data['']
    begin_date = data['']
    end_date = data['']
    order_begin_date = data['']
    order_end_date = data['']
    is_only_consumer_trigger = data[''] #是否仅支持顾客手动触发
    use_coupon_is_send_prize = data[''] #用券订单是否发奖
    is_plus_exclusive = data['']    #是否plus会员专享
    within_days = data['']  #订单搜索天数(顾客几天内领取)
    areas_scope = data['']  #订单奖励活动限制区域
    shops_scope = data['']  #订单奖励活动限制门店


    close_sshserver(server, dbconfig, cursor)
