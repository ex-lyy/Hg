# -*- encoding：utf-8 -*-
# 文件名称：Lyy-查询导购员销售额
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/10/9 下午 06:00

from 致维网络.joowMain import *

org_code = 'aiying'
guide_no = '2308'

# 查询导购今日销售金额
sales_performance, order_count = find_guider_daily_sale_amount(org_code, guide_no)
print("导购今日销售金额：\t", sales_performance, "元;\t\t导购今日订单数量：", order_count, '单。')

# 查询导购本月（今天凌晨之前）销售金额
sales_performance, order_count = find_guider_monthly_sale_amout(org_code, guide_no)
print("导购本月销售金额：\t", sales_performance, "元;\t\t导购本月订单数量：", order_count, '单。')

# 查询导购上月销售金额
sales_performance, order_count = find_guider_last_month_sale_amout(org_code, guide_no)
print("导购本上月销售金额：\t", sales_performance, "元;\t\t导购上月订单数量：", order_count, '单。')

# 查询导购智零售密码
password = decode_MD5(org_code, guide_no)
print("导购员的智零售登录密码密文为：", password)
