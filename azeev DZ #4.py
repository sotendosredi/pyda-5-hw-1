#!/usr/bin/env python
# coding: utf-8

# Задание 1. Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России.

# In[25]:


geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

input_country = input('Введите страну: ')
f_geo_log =[]
for i in range(len(geo_logs)):
    if input_country in list(dict.values(geo_logs[i]))[0]:
        f_geo_log.append(geo_logs[i])
        
print(f_geo_log)


# Задание 2. Выведите на экран все уникальные гео-ID из значений словаря ids. Т. е. список вида [213, 15, 54, 119, 98, 35]

# In[37]:


ids = {'user1': [213, 213, 213, 15, 213], 
       'user2': [54, 54, 119, 119, 119], 
       'user3': [213, 98, 98, 35]}

ids_new = []

for i in range(len(list(dict.values(ids)))):
     ids_new.extend(list(dict.values(ids))[i])
print(list(set(ids_new)))


# Задание 3. Дан список поисковых запросов. Получить распределение количества слов в них. Т. е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

# In[76]:


queries = [
    'смотреть сериалы онлайн сериалы про спорт про спорт сериалы про',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'сериалы про спорт про спорт'
]

import math

units = {1:'одного', 2:'двух',
         3:'трех', 4:'четырех',
         5:'пяти', 6:'шести', 
         7:'семи', 8:'восьми',
         9:'девяти'}

ten = {10:'десяти', 11:'одинадцати',
       12:'двенадцати', 13:'тринадцати',
       14:'четырнадцати', 15:'пятнадцати', 
       16:'шестнадцати', 17:'семнадцати',
       18:'восемнадцати', 19:'девятнадцати'}

even_dozens = {20:'двадцати', 30:'тридцати',
               40:'сорока', 50:'пятидесяти',
               60:'шестидесяти', 70:'пятнадцати', 
               80:'восьмидесяти', 90:'девяноста'}

centurions = {}

from collections import Counter

len_queries = []

for i in range(len(queries)):
    len_queries.append(len(queries[i].split()))
b = sorted(Counter(len_queries).items(), key=lambda x:x[1])
b.sort()

if b[0][0] == 1:
    print('Поисковых запросов из одного - слова', round(b[0][1]/int(len(queries)),2)*100,'%', end='')
else:
    print('Поисковых запросов из одного - слова 0 %', end='')

for i in range(len(b)):
    if len(str(b[i][0])) == 1:
        print(', из', units[b[i][0]], '-', round(b[i][1]/int(len(queries)),2)*100,'%', end='')
    elif 10 <= int(b[i][0]) <= 19:
        print(', из', ten[b[i][0]], '-', round(b[i][1]/int(len(queries)),2)*100,'%', end='')
    else:
        print(', из', even_dozens[math.floor(int(b[3][0])/10)*10], units[int((str(int(b[3][0])/10)).split('.')[1])],
              '-', round(b[i][1]/int(len(queries)),2)*100,'%', end='')


# Задание 4. Дана статистика рекламных каналов по объемам продаж. Напишите скрипт, который возвращает название канала с максимальным объемом. Т. е. в данном примере скрипт должен возвращать 'yandex'.

# In[80]:


stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
print('Канал с максимальным объемом продаж -',get_key(stats,max(stats.values())))


# Задание 5. Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100] (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}

# In[84]:


line =  ['2018-01-01', 'yandex', 'cpc', 100]
line.reverse()
line[0], line[1] = line[1], line[0]

for i in range(len(line)-1):
    line_ = {}
    line_[line[0]] = line[1]
    del line[0]
    del line[0]
    line.insert(1,line_)
line = line[0]
print(line)

