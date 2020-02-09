import csv
import json
import requests
from scrapy import Selector

class Processing:
    def pre_processing(self):
        response = requests.get('https://www.ipe.org.cn/MapGZBD/GZBDMap.html')
        selector = Selector(response=response)

        cityids = [x[13:-1] for x in selector.xpath('//div[@class="province-list"]/a/@onclick').extract()]
        citynames = [x.encode(response.encoding).decode("utf-8") for x in
                     selector.xpath('//div[@class="province-list"]/a/text()').extract()]
        # print(cityids, len(cityids))
        # print(citynames, len(citynames))

        with open('history/_city.csv', 'w', encoding='utf-8', newline='')as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(["provinceid", "provincename", "cityid", "cityname", "type"])

            for i in range(len(cityids)):
                temp = cityids[i].split(',')
                provinceid = temp[0]
                cityid = temp[1]
                type = temp[2]
                cityname = citynames[i]
                if "待确认" in cityname:
                    continue
                csvwriter.writerow([provinceid, "省份名称", cityid, cityname, type])

    def post_processing(self):
        cities = []
        with open('history/city.csv', 'r')as f:
            rows = csv.reader(f)
            next(rows)
            for row in rows:
                cities.append({"provinceid": row[0],
                               "provincename": row[1],
                               "cityid": row[2],
                               "cityname": row[3]})

        with open('history/merge.csv', 'w', encoding='utf-8', newline='')as mergefile:
            csvwriter = csv.writer(mergefile)
            firstcolumn = ["provinceid", "provincename", "cityid", "cityname",
                           "confirmed", "suspected", "dead", "cured", "updatetime"]
            csvwriter.writerow(firstcolumn)
            for city in cities:
                with open('history/{}_{}.json'.format(city["provinceid"], city["cityid"]), 'r')as f:
                    text = f.read()
                    js = json.loads(text)
                    # print(js)
                    confirmed = js["quezhendata"]
                    suspected = js["yisidata"]
                    dead = js["deaddata"]
                    cured = js["okdata"]
                    updatetime = js["timedate"]
                    for i in range(len(updatetime)):
                        csvwriter.writerow([city["provinceid"], city["provincename"], city["cityid"], city["cityname"],
                                            confirmed[i]["value"], suspected[i]["value"], dead[i]["value"], cured[i]["value"],
                                            updatetime[i].replace('.', '/')])

if __name__ == '__main__':
    pass
    P = Processing()
    P.post_processing()