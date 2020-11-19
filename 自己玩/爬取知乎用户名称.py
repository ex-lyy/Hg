# -*- coding:utf-8 -*-
# 文件名称：Lyy-爬取知乎用户名称
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/10/29 17:12

import requests
import pymysql


offset = 0
user_id = 'cong-qian-62'

request_url = 'https://www.zhihu.com/api/v4/articles/267832260/root_comments?order=normal&limit=20&offset=%s&status=open'%offset

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.11 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/json,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "cookie": '_zap=942bb2c0-25a8-48b7-ad1d-ef4d15bbc9c7; d_c0="AIAWHoEZGhKPTieN5lkcn3Qa6jgQ698eNZ0=|1603769161"; _xsrf=3516770b-ab87-469d-a25a-dce05d71121e; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1603880790,1603955407,1603955430,1603956359; SESSIONID=ajcbg9OMmYKRPcXL6DAsiMDPO8f3LHusrKHTrqdV9Cl; JOID=VV8SBEu0jAb2kqjVLrSrmee5ESU_1eZlk_KRmmPe1U2kxcyNYjLim6mVqNUpaJGzTPo6cQeRHS4oIXQ6Hd_ZM80=; osd=W14XC026jQP5lKbUK7utl-a8HiMx1ONqlfyQn2zY20yhysqDYzftnaeUrdovZpC2Q_w0cAKeGyApJHs8E97cPMs=; capsion_ticket="2|1:0|10:1603956410|14:capsion_ticket|44:OTI5M2UwOTYxMGJiNDlmYzhiOWUzMWEzZWU0MDZkYzk=|fc27d49e175b8678b2444b3d1afd851515dc4d95df51b0c765ed998a51e610e4"; z_c0="2|1:0|10:1603956411|4:z_c0|92:Mi4xVVAwSkF3QUFBQUFBZ0JZZWdSa2FFaVlBQUFCZ0FsVk51N3lIWUFETHIzWmVIeXlkYjluODF3RzdXb2tQTnZBZUZB|adfec6afcb6eb0d7db30916bc47983bca33afca03bc37314bfed4dea2f90d4a0"; tst=r; KLBRSID=031b5396d5ab406499e2ac6fe1bb1a43|1603962343|1603955406; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1603962344'
}
data={
    "include": "data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics",
    "offset": "20",
    "limit": "20"
}



res = requests.get(request_url,headers=headers,data=data)
res_member_count = res.json()['common_counts']
count_limit = round(res_member_count/20)*20

conn = pymysql.connect(host = 'localhost',port=3306,database='lyy',user='root',password='ex19950816')
cursor = conn.cursor()


for offset in range(0,count_limit+1,20):
    request_url = 'https://www.zhihu.com/api/v4/articles/267832260/root_comments?order=normal&limit=20&offset=%s&status=open'%offset
    res = requests.get(request_url, headers=headers, data=data)
    res_member_count = res.json()['common_counts']
    for i in res.json()['data']:
        user_name = i['author']['member']['name']
        user_word = i['author']['member']['headline']
        sql = f'''INSERT INTO zhihu_user_names (user_name,user_word,created_at) VALUE ('{user_name}','{user_word}',NOW());'''
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)

cursor.close()
conn.close()