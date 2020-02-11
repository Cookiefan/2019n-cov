# 2019n-cov
# 直接将ncov文件夹拷贝到项目中，并调用nocv.reader.get_data
## 请参考test.py的调用方法
## get_data(key='wuhan', start_date='2020-01-10', end_date='2020-02-10')
## 参数说明：
### key 地区字段，可选的有 ['guangdong', 'hubei', 'nation', 'shenzhen', 'wuhan']
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
## watch_data(key='wuhan', start_date='2020-01-10', end_date='2020-02-10')
### 增加数据查看功能
### 输入省、市、时间，打印这段时间内观察、确诊、死亡、痊愈的人数曲线