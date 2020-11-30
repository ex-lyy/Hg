# -*- coding:utf-8 -*-
# 文件名称：Hg-lyycc-test
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/11/24 16:40
from Mymain import *
import re

org_code = 'dyxinya'
activity_code = 'pe_1589620826768826'

# excel_name_time = get_time_str()
# # 存放结果的文件的绝对路径
# result_excel_path = r'C:\Users\LyyCc\Desktop\抽奖标准化-%s.xlsx' %excel_name_time
# # 有对应模板的excel文件执行load_excel,如果没有执行create_excel+load_excel
# print(result_excel_path)
# create_excel(result_excel_path)
# load_excel(result_excel_path)

def query_base_info():
    server, dbconfig, cursor = connect_master_copy_DB('pomelo_backend_production')

    base_info_query_sql = "SELECT id,org_code,code,name,begin_time,end_time FROM pomelo_backend_production.marketing_prize_events WHERE org_code='%s' AND code='%s';" % (
    org_code, activity_code)
    cursor.execute(base_info_query_sql)
    base_info = cursor.fetchone()
    print(base_info)
    close_sshserver(server, dbconfig, cursor)
    return base_info,base_info['id']


def query_count_info(activity_id):
    server, dbconfig, cursor = connect_master_copy_DB('pomelo_backend_production')

    base_info_query_sql = "SELECT seq,IFNULL(id, '总计') id,CONCAT(ROUND(SUM(probability),2),'%%') AS 概率,SUM(num) AS 数量,prize_name AS 奖品,backup As 备份奖励 FROM pomelo_backend_production.marketing_random_prizes WHERE prize_event_id = %s GROUP BY id WITH ROLLUP;" %activity_id
    cursor.execute(base_info_query_sql)
    base_info = cursor.fetchall()
    print(base_info)
    close_sshserver(server, dbconfig, cursor)
    return base_info

def query_serial_name(org_code,serial_no):
    server, dbconfig, cursor = connect_master_copy_DB('pomelo_backend_production')
    base_info_query_sql = "SELECT name FROM pomelo_backend_production.promotion_coupon_definitions WHERE org_code='%s' AND serial_no='%s';" %(org_code,serial_no)
    cursor.execute(base_info_query_sql)
    base_info_data = cursor.fetchone()

    close_sshserver(server, dbconfig, cursor)
    return  base_info_data['name']


def query_prize_info(activity_id):
    server, dbconfig, cursor = connect_master_copy_DB('pomelo_backend_production')
    base_info_query_sql = "SELECT * FROM pomelo_backend_production.marketing_random_prizes WHERE prize_event_id=%s;" %activity_id
    cursor.execute(base_info_query_sql)
    base_info_data = cursor.fetchall()
    close_sshserver(server, dbconfig, cursor)
    write_lines_data_list = []
    for base_info in base_info_data:
        write_lines_data_dict = {}
        prize_type = expiration_day = begin_date = end_date = serial_no = prize_name = max_price = min_price = 'NA'
        actions = eval(base_info['actions'])
        if len(actions) == 1 :
            actions = actions[0]
            if actions['type']== 'coupon':
                prize_type = '优惠券'
                if actions['params']['expiration_date_type'] == 'by_day':
                    expiration_day = actions['params']['expiration_day']
                    begin_date =''
                    end_date = ''
                    serial_no = actions['params']['serial_no']
                    prize_name = query_serial_name('jwbaby',serial_no)
                elif actions['params']['expiration_date_type'] == 'by_date':
                    expiration_day = ''
                    begin_date = actions['params']['begin_date']
                    end_date = actions['params']['end_date']
                    serial_no = actions['params']['serial_no']
                    prize_name = query_serial_name('jwbaby', serial_no)
            elif actions['type']== 'ticket':
                prize_type ='兑换券'
                if actions['params']['expiration_date_type'] == 'by_day':
                    expiration_day = actions['params']['expiration_day']
                    begin_date =''
                    end_date = ''
                    serial_no = actions['params']['activity_id']
                    prize_name_index = re.match("^\[[\s\S]*]",actions['prize_name']).span()[1]
                    prize_name = actions['prize_name'][prize_name_index:]
                elif actions['params']['expiration_date_type'] == 'by_date':
                    expiration_day = ''
                    begin_date = actions['params']['begin_date']
                    end_date = actions['params']['end_date']
                    serial_no = actions['params']['activity_id']
                    prize_name_index = re.match("^\[[\s\S]*]",actions['prize_name']).span()[1]
                    prize_name = actions['prize_name'][prize_name_index:]
            elif actions['type']== 'package':
                prize_type ='画像礼包'
                serial_no=actions['params']['code']
                prize_name = actions['prize_name']
            elif actions['type']== 'checkin_card':
                    expiration_date =actions['params']['expiration_date']
                    card_days = actions['params']['card_days']
            elif actions['type']== 'coupon_bag':
                prize_type ='礼券包'
                if actions['params']['expiration_date_type'] == 'by_day':
                    expiration_day = actions['params']['expiration_day']
                    begin_date = ''
                    end_date = ''
                    serial_no = actions['params']['code']
                    prize_name = actions['prize_name']
                elif actions['params']['expiration_date_type'] == 'by_date':
                    expiration_day = ''
                    begin_date = actions['params']['begin_date']
                    end_date = actions['params']['end_date']
                    serial_no = actions['params']['code']
                    prize_name = actions['prize_name']
            elif actions['type']== 'intelligent_package':
                prize_type ='智能礼包'
                serial_no=actions['params']['code']
            elif actions['type']== 'red_pack':
                prize_type ='微信红包'
                max_price =  actions['params']['max_price']
                min_price =  actions['params']['min_price']
                prize_name = actions['prize_name']
            elif actions['type']== 'red_envelope':
                prize_type = '商城红包'
                max_price = actions['params']['max_price']
                min_price = actions['params']['min_price']
                prize_name = actions['prize_name']
            else:
                pass

        write_lines_data_dict['prize_type'] = prize_type
        write_lines_data_dict['expiration_day'] = expiration_day
        write_lines_data_dict['begin_date'] = begin_date
        write_lines_data_dict['end_date'] = end_date
        write_lines_data_dict['serial_no'] = serial_no
        write_lines_data_dict['prize_name'] = prize_name
        write_lines_data_dict['max_price'] = max_price
        write_lines_data_dict['min_price'] = min_price
        write_lines_data_list.append(write_lines_data_dict)
    return write_lines_data_list




