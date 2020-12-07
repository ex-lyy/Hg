from Mymain import *
import json

# 查询礼券包基本信息
def query_couponbag_info(org_code,package_code):
    query_couponbag_info_sql = "SELECT total,`name`,optional,`desc`,related_coupon,prize_items FROM pomelo_backend_production.prize_coupon_bags WHERE org_code='%s' AND code='%s';"%(org_code,package_code)
    server, dbconfig, cursor = connect_master_copy_DB('pomelo_backend_production')
    cursor.execute(query_couponbag_info_sql)
    couponbag_info_sql_data = cursor.fetchone()
    close_sshserver(server, dbconfig, cursor)
    if couponbag_info_sql_data['related_coupon'] != '{"type": "", "params": {}, "valid_days": 7, "offset_days": 1}':
        print("礼券包‘%s‘配置的有领取后关联优惠，请进行额外的检查!"%couponbag_info_sql_data['name'])
    couponbag_base_info = copy.deepcopy(couponbag_info_sql_data)
    couponbag_base_info.pop('related_coupon')
    couponbag_base_info.pop('prize_items')
    couponbag_info_list = []
    # 处理配置的奖励数据
    couponbag_prize_items = json.loads(couponbag_info_sql_data['prize_items'])
    for prize_items in couponbag_prize_items:
        prize_items_dict = {'type':'优惠券','serial_no':'','serial_name':'','min_price':'','max_price':''}   #定义字典，储存我们配置的每一项的数据
        if prize_items['type']  == 'coupon':
            prize_items_dict['type'] = '优惠券'
            prize_items_dict['serial_no'] = prize_items['params']['serial_no']
            prize_items_dict['serial_name'] = prize_items['prize_name']
        elif prize_items['type']  == 'ticket':
            prize_items_dict['type'] = '兑换券'
            prize_items_dict['serial_no'] = prize_items['params']['activity_id']
            prize_items_dict['serial_name'] = prize_items['params']['name']
        elif prize_items['type']  == 'virtual_product':
            prize_items_dict['type'] = '积分'
            prize_items_dict['score_num'] = prize_items['params']['num']
            prize_items_dict['serial_name'] = prize_items['prize_name']
        elif prize_items['type']  == 'red_envelope':
            prize_items_dict['type'] = '红包'
            prize_items_dict['min_price'] = prize_items['params']['min_price']
            prize_items_dict['max_price'] = prize_items['params']['max_price']
            prize_items_dict['serial_name'] = prize_items['prize_name']
        elif prize_items['type']  == 'intelligent_package':
            prize_items_dict['type'] = '会员智能礼包'
            prize_items_dict['name'] = 'NA'
            prize_items_dict['serial_no'] = prize_items['params']['code']
        else:
            print("礼券包%s出现了点问题，请手动检查！"%couponbag_info_sql_data['name'])
        couponbag_info_list.append(prize_items_dict)
    # 返回活动基本信息、活动配置的奖励信息
    return couponbag_info_sql_data,couponbag_info_list


couponbag_info_sql_data, couponbag_info_list = query_couponbag_info('jwbaby', 'coupon_bag_20200813101018')
print(couponbag_info_sql_data)
print(couponbag_info_list)