from Mymain import *
import json


# 查询配置的奖励信息
def query_avtivity_prize_info(org_code, activity_id):
    query_avtivity_prize_info_sql = "select reward_limit,max_count,prize_type,prize_info,member_restriction_count,member_restriction,restriction_product_skus from pomelo_backend_production.rush_to_get_coupon_prize_items where org_code='%s' and activity_id= '%s' order by priority desc;" % (
    org_code, activity_id)
    server, dbconfig, cursor = connect_master_copy_DB('pomelo_backend_production')
    cursor.execute(query_avtivity_prize_info_sql)
    activity_prize_info_data = cursor.fetchall()
    close_sshserver(server, dbconfig, cursor)
    activity_prize_item_list = []
    for activity_prize_item in activity_prize_info_data:
        limit_type = limit_count = prize_type = prize_serial_no = prize_serial_name = expiration_date = prize_begin_date = prize_end_date = prize_get_limit_type = prize_get_limit_skus = '-'
        activity_prize_item_dict = {}
        # 划分限制类型
        if activity_prize_item['reward_limit'] == 'total':
            limit_type = '限制总量'
        elif activity_prize_item['reward_limit'] == 'none':
            limit_type = '不限制'
        elif activity_prize_item['reward_limit'] == 'day':
            limit_type = '每日限量'
        limit_count = activity_prize_item['max_count']
        # 划分奖励类型
        if activity_prize_item['prize_type'] == 'coupon':
            prize_type = '优惠券'
            activity_prize_item_info = json.loads(activity_prize_item['prize_info'])
            if activity_prize_item_info['params']['expiration_date_type'] == 'by_day':
                expiration_date = activity_prize_item_info['params']['expiration_date']
            elif activity_prize_item_info['params']['expiration_date_type'] == 'by_date':
                prize_begin_date = activity_prize_item_info['params']['begin_date']
                prize_end_date = activity_prize_item_info['params']['end_date']
            prize_serial_no = activity_prize_item_info['params']['serial_no']
            prize_serial_name = activity_prize_item_info['prize_name']
        elif activity_prize_item['prize_type'] == 'ticket':
            prize_type = '兑换券'
            activity_prize_item_info = json.loads(activity_prize_item['prize_info'])
            if activity_prize_item_info['params']['expiration_date_type'] == 'by_day':
                expiration_date = activity_prize_item_info['params']['expiration_date']
            elif activity_prize_item_info['params']['expiration_date_type'] == 'by_date':
                prize_begin_date = activity_prize_item_info['params']['begin_date']
                prize_end_date = activity_prize_item_info['params']['end_date']
            prize_serial_no = activity_prize_item_info['id']
            prize_serial_name = activity_prize_item_info['params']['name']
        elif activity_prize_item['prize_type'] == 'coupon_bag':
            prize_type = '礼券包'
            activity_prize_item_info = json.loads(activity_prize_item['prize_info'])
            if activity_prize_item_info['params']['expiration_date_type'] == 'by_day':
                expiration_date = activity_prize_item_info['params']['expiration_date']
            elif activity_prize_item_info['params']['expiration_date_type'] == 'by_date':
                prize_begin_date = activity_prize_item_info['params']['begin_date']
                prize_end_date = activity_prize_item_info['params']['end_date']
            prize_serial_no = activity_prize_item_info['params']['code']
            prize_serial_name = activity_prize_item_info['prize_name']
        # 判断券领取限制
        if activity_prize_item['member_restriction'] == 'all':
            prize_get_limit_type = '不限制'
        elif activity_prize_item['member_restriction'] == 'not_buy_product':
            prize_get_limit_type = '限制未购条码'
            prize_get_limit_skus = activity_prize_item['restriction_product_skus']
        activity_prize_item_dict['limit_type'] = limit_type
        activity_prize_item_dict['limit_count'] = limit_count
        activity_prize_item_dict['prize_type'] = prize_type
        activity_prize_item_dict['prize_serial_no'] = prize_serial_no
        activity_prize_item_dict['expiration_date'] = expiration_date
        activity_prize_item_dict['prize_begin_date'] = prize_begin_date
        activity_prize_item_dict['prize_end_date'] = prize_end_date
        activity_prize_item_dict['prize_get_limit_type'] = prize_get_limit_type
        activity_prize_item_dict['prize_get_limit_skus'] = prize_get_limit_skus
        activity_prize_item_list.append(activity_prize_item_dict)
    return activity_prize_item_list


cc = query_avtivity_prize_info('jwbaby', 6055)

print(cc)