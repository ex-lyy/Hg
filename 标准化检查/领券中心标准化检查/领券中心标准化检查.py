# -*- coding:utf-8 -*-
# 文件名称：Hg-lyycc-领券中心标准化检查
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/12/7 10:41

import openpyxl
from Mymain import *
from openpyxl.styles import Font, colors, Alignment,PatternFill,Border, Side


def create_excel(result_excel_path):
    # 生成指定路径的Excel文件(此步骤只能进行生成工作，本次的表格对象是只读模式)
    wb = openpyxl.Workbook(result_excel_path)
    ws1 = wb.create_sheet('领券中心标准化检查结果')
    ws2 = wb.create_sheet('领券中心标准化检查描述')
    wb.save(result_excel_path)
    return 0

def write_medoel_excel(result_excel_path):
    wb = openpyxl.load_workbook(result_excel_path)
    ws = wb['领券中心标准化检查结果']
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=10)
    ws.merge_cells(start_row=5, start_column=1, end_row=5, end_column=10)
    ws.merge_cells(start_row=19, start_column=1, end_row=19, end_column=10)
    ws.merge_cells(start_row=32, start_column=1, end_row=32, end_column=10)
    cell_list = ['1','5','19','32']
    ws['A1'] = '活动基本信息'
    ws['A5'] = '奖励概率及数量信息'
    ws['A19'] = '配置的奖励信息'
    ws['A32'] = '奖励等级信息'

    ws = make_cell_style(cell_list,ws)
    ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
    ws['A5'].alignment = Alignment(horizontal='center', vertical='center')
    ws['A19'].alignment = Alignment(horizontal='center', vertical='center')
    ws['A32'].alignment = Alignment(horizontal='center', vertical='center')
    # 写模板数据-活动基本信息
    ws.cell(row= 2 ,column= 1,value='ID')
    ws.cell(row= 2 ,column= 2,value='商户code')
    ws.cell(row= 2 ,column= 3,value='活动code')
    ws.cell(row= 2 ,column= 4,value='活动名称')
    ws.cell(row= 2 ,column= 5,value='活动开始时间')
    ws.cell(row= 2 ,column= 6,value='活动结束时间')
    # 写模板数据-中奖概率及数量
    ws.cell(row= 6 ,column= 1,value='奖励序号')
    ws.cell(row= 6 ,column= 2,value='奖励ID')
    ws.cell(row= 6 ,column= 3,value='概率（百分比）')
    ws.cell(row= 6 ,column= 4,value='数量')
    ws.cell(row= 6 ,column= 5,value='奖项名称')
    ws.cell(row= 6 ,column= 6,value='是否是备份奖励')
    # 写模板数据-配置的奖励信息
    ws.cell(row= 20 ,column= 1,value='奖励类型')
    ws.cell(row= 20 ,column= 2,value='奖励名称')
    ws.cell(row= 20 ,column= 3,value='中奖描述')
    ws.cell(row= 20 ,column= 4,value='奖励编号')
    ws.cell(row= 20 ,column= 5,value='固定天数')
    ws.cell(row= 20 ,column= 6,value='奖励开始时间')
    ws.cell(row= 20 ,column= 7,value='结束时间')
    ws.cell(row= 20 ,column= 8,value='最大红包金额')
    ws.cell(row= 20 ,column= 9,value='最小红包金额')
    # 写模板数据-写奖励等级信息
    ws.cell(row= 33 ,column= 1,value='type')
    ws.cell(row= 33 ,column= 2,value='活动id')
    ws.cell(row= 33 ,column= 3,value='等级id')
    ws.cell(row= 33 ,column= 4,value='奖励')
    wb.save(result_excel_path)
    return 0

# 定义顶层模板样式
def make_cell_style(cell_list,ws):
    cell_row_list = ['A','B','C','D','E','F','G','H','I','J']
    cell_font = Font(u'宋体',size = 11,bold=True,italic=False,strike=False)
    cell_fill = PatternFill("solid", fgColor="ffa64d")
    cell_border = Border(top=Side(border_style='thin', color=colors.BLACK),
                    bottom=Side(border_style='thin', color=colors.BLACK),
                    left=Side(border_style='thin', color=colors.BLACK),
                    right=Side(border_style='thin', color=colors.BLACK))
    for cell in cell_list:
        for cell_row in cell_row_list:
            ws[cell_row+cell].font = cell_font
            ws[cell_row+cell].fill = cell_fill
            ws[cell_row+cell].border = cell_border
            ws.column_dimensions[cell_row].width = 27.5
    return ws


# 查询活动基本信息
def query_avtivity_base_info(org_code,activity_code):
    query_avtivity_base_info_sql= "SELECT id,name,code,description,begin_date,end_date,cycle_type,active_dates,limit_config,shareable,new_member_able,visibility FROM pomelo_backend_production.rush_to_get_coupon_activities WHERE org_code='%s' AND code='%s';"%(org_code,activity_code)
    server, dbconfig, cursor = connect_master_copy_DB('pomelo_backend_production')
    cursor.execute(query_avtivity_base_info_sql)
    avtivity_base_info_data = cursor.fetchone()
    close_sshserver(server, dbconfig, cursor)
    if avtivity_base_info_data['cycle_type']== 'none':
        return avtivity_base_info_data
    else:
        print("周期性领券中心，暂时未处理")

# 查询配置的奖励信息
def query_avtivity_prize_info(org_code,activity_id):
    query_avtivity_prize_info_sql= "select reward_limit,max_count,prize_type,prize_info,member_restriction_count,member_restriction,restriction_product_skus from pomelo_backend_production.rush_to_get_coupon_prize_items where org_code='%s' and activity_id= '%s' order by priority desc;"%(org_code,activity_id)
    server, dbconfig, cursor = connect_master_copy_DB('pomelo_backend_production')
    cursor.execute(query_avtivity_prize_info_sql)
    avtivity_prize_info_data = cursor.fetchall()
    close_sshserver(server, dbconfig, cursor)
    return avtivity_prize_info_data


if __name__ == '__main__':
    org_code = 'jwbaby'
    activity_code = 'gc_1607309295950189'

    # excel_name_time = get_time_str()
    # # 存放结果的文件的绝对路径
    # result_excel_path = r'C:\Users\LyyCc\Desktop\抽奖标准化-%s.xlsx' %excel_name_time
    # # 有对应模板的excel文件执行load_excel,如果没有执行create_excel+load_excel
    # print("当前工作文件路径为：",result_excel_path)    # 输出当前文件路径
    # # 创建文件并写入标准模板
    # create_excel(result_excel_path)
    # write_medoel_excel(result_excel_path)

    avtivity_base_info_data = query_avtivity_base_info(org_code,activity_code)
    activity_id = avtivity_base_info_data['id']
    avtivity_prize_info_data = query_avtivity_prize_info(org_code,activity_id)
    for avtivity_prize_items in avtivity_prize_info_data:
        print(avtivity_prize_items)
    couponbag_info_sql_data, couponbag_info_list = query_couponbag_info('jwbaby', 'coupon_bag_20200813101018')

