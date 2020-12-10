import time
from multiprocessing import pool
import requests
import random



headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Length': '0',
    'Host': 'weixinqa03.joowing.com',
    'Referer': 'https://weixinqa03.joowing.com/org/joowing/prize_events/multiple_retailer_prize_event_1600852407944817/play?c_type=62&c_code=multiple_retailer_prize_event_1600852407944817&',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Cookie': 'Hm_lvt_0c2e41563784bcc9e3dabc630b67ef35=1598250593; _ga=GA1.2.1246383103.1598250597; _pomelo_session=f612330455a2beb49d763b63ac2f0c0d; tyfish_user_id=3e854ea0-f9f8-0137-e779-0242ac1e1212; cwdtest_user_id=064740c0-4b20-0138-050c-0242ac1e1509; __51cke__=; joowing_user_id=584bf1d0-b2ad-0137-395c-0242ac1e6869; __tins__19853273=%7B%22sid%22%3A%201600862568110%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201600865864400%7D; __51laig__=16'
}
url1 = 'https://weixinqa03.joowing.com/org/joowing/prize_events/multiple_retailer_prize_event_1600863874261106/over.json'
data = None

pool_list = []
for a in range(20):
    pool_list.append(a)
print(pool_list)


def send_prize(i):
    randtime = random.randint(1, 40)
    # time.sleep(randtime)
    # i += 1
    # print(f"第{i}次抽奖")
    res = requests.post(url=url1, headers=headers, data=data)
    print(res)

pool_size = 50
pool = pool.ThreadPool(pool_size)  # 创建一个线程池
pool.map(send_prize, pool_list)  # 往线程池中填线程
pool.close()  # 关闭线程池，不再接受线程
pool.join()  # 等待线程池中线程全部执行完