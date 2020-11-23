# -*- coding:utf-8 -*-
# 文件名称：Hg-lyycc-订单奖励标准化检查
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/11/19 18:19

from Mymain import *
import openpyxl

# 判断奖励依据的类型
def check_activity_order_condition_type(check_value):
        if check_value == 'total':
            check_value = '单笔订单金额'
            order_grade_flag = 1
        elif check_value == 'current':
            check_value = '单笔订单数量'
            order_grade_flag = 1
        elif check_value == 'current_accumulative':
            check_value = '单笔订单每满数量'
            order_grade_flag = 0
        elif check_value == 'accumulative':
            check_value = '多笔订单累计每满数量'
            order_grade_flag = 0
        return check_value,order_grade_flag

# 判断奖励依据的类型-单内商品
def check_activity_order_condition_type_first(check_value):
    if check_value == 'current':
        check_value = '订单金额满（只获取最大档次奖励）'
        order_grade_flag = 1
    elif check_value == 'current_accumulative':
        check_value = '订单金额每满'
        order_grade_flag = 0
    elif check_value == 'accumulative_not_repeat':
        check_value = '订单金额累计满'
        order_grade_flag = 1
    elif check_value == 'accumulative':
        check_value = '订单金额累计每满'
        order_grade_flag = 0
    return check_value,order_grade_flag

# 品类映射
def category_translation(category_list):
    category_translation_list = []
    # 定义品类列表：
    category_dict = {'01':'奶粉','02':'营养保健','03':'尿布尿裤','04':'童装童鞋','05':'喂养用品','06':'洗护用品','07':'车床出行','08':'玩具文娱','09':'妈妈用品','10':'婴儿棉品','11':'辅食零食','18':'服务类','90':'其他','91':'折扣类','93':'非销售（不计入大盘销售）'}
    for category in category_list:
        category_translation_list.append(category_dict[category.replace("'",'"')])
    return category_translation_list

# 奖励类型映射
def prize_type_translation(prize_items_range):
    if prize_items_range['type'] == 'coupon':
        prize_type = '优惠券'
        serial_number = prize_items_range['prize_items_range']
        serial_no = prize_items_range['serial_no']
        expiration_date_type = prize_items_range['expiration_date_type']
        if expiration_date_type == 'by_day':
            begin_date = "奖励发放当天起"
            end_date = prize_items_range['expiration_day']

        else:
            begin_date = prize_items_range['begin_date']
            end_date = prize_items_range['end_date']

        return prize_type,serial_number,serial_no,begin_date,end_date



org_code='jwbaby'
activity_code='prize_activity_1605866593626036'

if __name__ == '__main__':
    # 链接公网备库
    server, dbconfig, cursor = connect_master_copy_DB("pomelo_backend_production")
    # 查询订单奖励数据
    activity_Sql = f'''SELECT * FROM pomelo_backend_production.prize_activities WHERE org_code = '{org_code}' AND CODE ='{activity_code}';'''
    cursor.execute(activity_Sql)
    activity_data = cursor.fetchone()   #获取订单奖励的数据，目前只做单活动查询
    # 关闭数据库链接
    close_sshserver(server, dbconfig, cursor)

    name = activity_data['name']    #活动名称
    begin_date = activity_data['begin_date']    #活动开始时间
    end_date = activity_data['end_date']    #活动结束时间
    order_begin_date = activity_data['order_begin_date']    #订单读取开始时间
    order_end_date = activity_data['order_end_date']    #订单读取结束时间
    within_days = activity_data['within_days']  # 顾客必须几天内领取
    # 判断是否仅顾客领取
    is_only_consumer_trigger = activity_data['is_only_consumer_trigger']  # 是否仅支持顾客手动触发
    if is_only_consumer_trigger== 1:
        is_only_consumer_trigger_describ = f'''是，{within_days}天内领取'''
    else:
        is_only_consumer_trigger_describ = f'''否'''
    use_coupon_is_send_prize = activity_data['use_coupon_is_send_prize']    #用券订单是否发奖
    is_plus_exclusive = activity_data['is_plus_exclusive']    #是否plus会员专享
    # 判断订单读取范围
    range = activity_data['range']    #订单读取范围
    if range == 'offline':
        range = '全部订单'
    elif range=='online':
        range = "仅线上订单"
    rule = eval(activity_data['rule'])    #活动规则
    prize_items = activity_data['prize_items']    #奖励内容
    state = activity_data['state']    #活动状态
    areas_scope = activity_data['areas_scope']    #限制区域
    shops_scope = activity_data['shops_scope']    #限制门店
    # 订单奖励依据
    activity_order_type = rule['basis']
    # 订单奖励条件
    activity_order_condition = rule['condition']
    # 判断奖励依据条件及类型
    if activity_order_type == 'order':
        activity_order_type = '单内商品'
        activity_order_condition_type,order_grade_flag =check_activity_order_condition_type_first(activity_order_condition['type'])
        # 参与的奖励条码
        skus = include_skus = activity_order_condition['include_skus']
        # 排除的奖励条码
        exclude_skus = activity_order_condition['exclude_skus']
        # 参与的品类条码
        include_cates = activity_order_condition['include_cates']
        include_cates = category_translation(include_cates)
        # 不参与的品类条码
        exclude_cates = activity_order_condition['exclude_cates']
        exclude_cates = category_translation(exclude_cates)
    elif activity_order_type == 'item':
        activity_order_type = '单内商品'
        activity_order_condition_type,order_grade_flag =check_activity_order_condition_type(activity_order_condition['type'])
    elif activity_order_type == 'new_client':
        activity_order_type = '品牌新客'
        activity_order_condition_type,order_grade_flag = check_activity_order_condition_type(activity_order_condition['type'])
    else:
        print('*'*30,'数据均不符合！','*'*30)
    # 活动奖励最大可获取次数
    limit_count = rule['count']
    # 每月最大可获取次数
    limit_monthly_count = rule['monthly_count']
    # 每天最大可获取次数
    limit_daily_count = rule['daily_count']
    # 奖励档次及资源：
    prize_items_range = activity_order_condition['prize_items_range']
    if order_grade_flag == 1:
        order_grade_list = []
        for order_grade in prize_items_range:
            order_grade_list.append(order_grade)
            prize_type, serial_number, serial_no, begin_date, end_date = prize_type_translation(prize_items_range)

    # 标准化检查描述
    if activity_order_type == '单内商品':
        activity_describ = f'''1.活动名称\n  {name}[{activity_code}]\n2.活动开始时间、订单读取时间\n  ({begin_date} ~ {end_date})\n  ({order_begin_date} ~ {order_end_date})\n3.订单读取范围\n  {range}\n4.是否需要顾客自己去领奖不领奖系统晚上统一下发\n  {is_only_consumer_trigger_describ}\n5.活动范围（门店、区域） 注意限制了门店区域就不要在填写\n  区域：{areas_scope.strip('"')}\n  门店：\n6.活动期间限制次数\n  最大可获取：{limit_count}次；\n7.每月、每天限制次数\n  每月最大可获取：{limit_monthly_count}次；每天最大可获取{limit_daily_count}次；\n8.参与的品类、商品\n  商品条码：{skus}\n  品类条码：{include_cates}\n9.不参与的品类、商品\n  不参与的商品条码：{exclude_skus}\n  不参与的商品品类：{exclude_cates}\n10.奖励下发方式（什么场景下下发什么奖励）\n11.代金券、兑换券奖励参考其检查模板\n12.联系AM线下实际出单测试\n13.规则描述、各奖励描述必填。\n  {activity_order_type}-{activity_order_condition_type}-{order_grade_list}'''
    else:
        # activity_describ = f'''1.活动名称\n  {name}[{activity_code}]\n2.活动开始时间、订单读取时间\n  ({begin_date} ~ {end_date})\n  ({order_begin_date} ~ {order_end_date})\n3.订单读取范围\n  {range}\n4.是否需要顾客自己去领奖不领奖系统晚上统一下发\n  {is_only_consumer_trigger_describ}\n5.活动范围（门店、区域） 注意限制了门店区域就不要在填写\n  {areas_scope.strip('"')}\n6.活动期间限制次数\n  最大可获取：{limit_count}次；\n7.每月、每天限制次数\n  每月最大可获取：{limit_monthly_count}次；每天最大可获取{limit_daily_count}次；\n8.参与的品类、商品\n  商品条码：{skus}\n9.不参与的品类、商品\n10.奖励下发方式（什么场景下下发什么奖励）\n11.代金券、兑换券奖励参考其检查模板\n12.联系AM线下实际出单测试\n13.规则描述、各奖励描述必填。\n  {activity_order_type}-{activity_order_condition_type}'''
        activity_describ = ''
    print(activity_describ)
    # print(shops_scope)
    # print(prize_items)