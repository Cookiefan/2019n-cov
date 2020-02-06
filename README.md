# 2019n-cov
# 直接将ncov文件夹拷贝到项目中，并调用nocv.reader.get_data
## 请参考test.py的调用方法
## get_data(province='', city='', start_date='2020-01-10', end_date='2020-02-03')
## 参数说明：
### province 空为全国数据
### city 空为全省数据
### 目前只有全国，广东省和湖北省各市的数据
## 返回列名：
### time 日期
### city 城市
### accumulated_confirmed 累积确诊人数
### accumulated_death 累积死亡人数
### accumulated_recovered 累积痊愈人数
### new_confirmed 新增确诊人数
### new_death 新增死亡人数
### new_recovered 新增痊愈人数