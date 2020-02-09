import csv
from data_processing import Processing
import requests
import tqdm
import random
import time


class Get_Ipe:
    def get_ipe(self, type=3, spaceid=228):
        cookies = {
            'acw_tc': '65c86a0915809070166357618ee03b6ad743f9590e8cfaf2c97115c9f4f08f',
            'SERVERID': '8abfb74b5c7dce7c6fa0fa50eb3d63af|1580908079|1580907016',
        }

        headers = {
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.ipe.org.cn',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://www.ipe.org.cn/MapGZBD/GZBDMap.html',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        params = (
            ('xx', 'getcity_chart'),
        )

        data = {
            'headers[Cookie]': 'SERVERID=8abfb74b5c7dce7c6fa0fa50eb3d63af|1580908079|1580907016',
            'cmd': 'getcity_chart',
            'type': str(type),
            'spaceid': str(spaceid)
        }
        while True:
            try:
                response = requests.post('https://www.ipe.org.cn/data_ashx/GetAirData.ashx', headers=headers,
                                         params=params,
                                         cookies=cookies, data=data)
                time.sleep(random.randint(20, 40))
                break
            except requests.exceptions.ConnectionError as err:
                print("[requests error]:", err)

        return response.text


if __name__ == '__main__':
    P = Processing()
    # P.pre_processing() # 还需手动改city.csv中的省份名称

    cities = []
    with open('history/city.csv', 'r', encoding='utf-8')as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            cities.append({"provinceid": row[0],
                           "provincename": row[1],
                           "cityid": row[2],
                           "cityname": row[3],
                           "type": row[4]})

    G = Get_Ipe()
    for city in tqdm.tqdm(cities):
        text = G.get_ipe(type=city["type"], spaceid=city["cityid"])
        text = text.replace('value', '"value"')
        text = text.replace('label', '"label"')
        text = text.replace('show', '"show"')
        text = text.replace('position', '"position"')
        text = text.replace('\'', '"')
        print(city["cityid"], city["cityname"], end='')
        with open('history/{}_{}.json'.format(city["provinceid"], city["cityid"]), 'w', encoding='utf-8') as f:
            f.write(text)

    P.post_processing()
