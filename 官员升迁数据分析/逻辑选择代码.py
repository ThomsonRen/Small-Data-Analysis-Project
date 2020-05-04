
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

data = pd.read_excel('Full Data.xlsx',sheet_name = '全部经历')

def clean_time(x):
    try:
        return int(x.year)
    except:
        return int(-1)

data['终止时间（（YYYY-MM-DD））'] = data['终止时间（（YYYY-MM-DD））'].apply(clean_time)


# In[3]:


cities = data['地方二级关键词'].unique()
c_List = []
PROMO_list = []
PROMO_IN_list = []
for city in cities:
    c_List.append(city)
    city_data = data[data['地方二级关键词'] == city]
    candidate_data = city_data[((city_data['标志位']  == '市委书记') | (city_data['标志位']  == '市长')) & 
                           (city_data['终止时间（（YYYY-MM-DD））'] < 2010)]
    name_list = candidate_data['姓名'].unique()
    flag = False
    flag2 = False
    for name in name_list:
        print(name)
        This_people_data = data[data['姓名'] == name]
        level_data = This_people_data[This_people_data['终止时间（（YYYY-MM-DD））'] > 2009]['级别']
        for l in level_data:
            if l in ['副部','正部','副国','正国']:
                flag = True
                break
        if flag == True:
            break  
    PROMO_list.append(flag)
    PROMO_IN_list.append(flag2)
Result = pd.DataFrame()
Result['CITY'] = cities
Result['PROMO'] = PROMO_list
Result['PROMO_IN'] = PROMO_IN_list

