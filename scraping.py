# from pytrends.request import TrendReq
import pandas as pd
import csv

# pytrends = TrendReq(hl='en-US')
df = pd.read_csv("word.csv",encoding='windows-1256')
num = len(df)
b = 0
# print(df)
print(df['word'][0])
ahmed = open('test.csv', 'w', encoding='UTF-8')


csv_columns = ['word']
#
writer = csv.DictWriter(ahmed, fieldnames=csv_columns)
writer.writeheader()

while  num > b:



    b+=1
ahmed.close()







# all_keywords = ['ahmed', 'bashar','obida','adnan','mohamed','salah','maha','dalia','eman']
# keywords = ['bashar', 'ahmed']
#
# timeframes = ['today 5-y', 'today 12-m',
#               'today 3-m', 'today 1-m']
# cat = ''
# geo = ''
# gprop = ''
#
# countries = ['india', 'united_states', 'united_kingdom',
#              'netherlands', 'brazil']
#
# #
# def check_trends():
#     pytrends.build_payload(kw_list = df['word'][0],
#                            cat=0,
#                            timeframe=timeframes[1],
#                            geo='',
#                            gprop='')
#     data = pytrends.related_queries()
#     print(data)
#
# check_trends()
#
#
#

