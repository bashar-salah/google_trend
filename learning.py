import pandas as pd
from pytrends.request import TrendReq
import json
"here to take obj for all req <===============>"
# here focus in  the encoding for arabic language "////windows-1256\\\"
df = pd.read_csv("word.csv", encoding='windows-1256')
pytrends = TrendReq(hl='en-US')

"here divide the file into five key in one list and all in one list  <===============> "

length = len(df)
start_point = 0
staying = length % 5
all_key = []
key = []
count = 0
all_count = 0
for a in df['word']  :
    key.append(a)
    count += 1
    all_count +=1
    if count == 5 or all_count == length  :
        count = 0
        all_key.append(key)
        key = []


"here all inf for scraping process <===============>"


timeframes = ['today 5-y', 'today 12-m',
              'today 3-m', 'today 1-m',]
cat = ''
geo = ['','Saudi Arabia']
gprop = ''
data  = ''

countries = ['india', 'united_states', 'united_kingdom',
             'netherlands', 'brazil']

"here create json file to add the data into it <===============> "

result = []
name_key = []
for a  in all_key :
    pytrends.build_payload(kw_list=a,
                               cat=0,
                               timeframe=timeframes[1],
                               geo=geo[0],
                               gprop='')
    data = pytrends.related_queries()
    result.append(data)
    name_key.append(a)
    # print(data)

    # print(data['محمد']['top'])
    # break


print(type(result[0]['محمد']['top'].query))
print("======================?")
print(result[0]['محمد']['top'].value[0])
# print(result)
# for a in data  :
#     pass
#     "here when print the a  the result is name of key "
#     print(a)
#     "here when print the data[a] the result is the quary without the name of key "
#     # print(data[a])
#
