#!/usr/bin/env python
# coding: utf-8
Задача 1. Дано слово из латинских букв. Напишите скрипт, который выводит на экран букву из середины слова (если число букв нечетное). Если букв четное число, то на экран выводятся две буквы из середины.  
# In[12]:


user_input_text = input('Введие текст:')

count_len_ut = len(user_input_text)
str_center = int(round(count_len_ut / 2,0))
help_point = int(str_center - 1)
if count_len_ut % 2 == 0:
    print(user_input_text[help_point] + user_input_text[str_center])
else:
    print(user_input_text[str_center])


# Задача 2. Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек (их число может варьироваться):
# 
# Идеальные пары:
# Alex и Emma
# Arthur и Kate
# John и Kira
# Peter и Liza
# Richard и Trisha
# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки! "Познакомить" пары нам поможет функция zip, а в цикле распакуем zip-объект и выведем информацию в виде:
# 
# Идеальные пары:
# Alex и Emma
# Arthur и Kate
# John и Kira
# Peter и Liza
# Richard и Trisha
# 
# Внимание! Если количество людей в списках будет не совпадать, то мы никого знакомить не будет и выведем пользователю предупреждение, что кто-то может остаться без пары!

# In[63]:


# по какой-то причине программа корректно не работает в jupyter. Через IDLE все получилось.
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys.sort()
girls.sort()
if len(boys) == len(girls):
    print('Идеальные пары:')
    for i, j in zip(boys, girls):
        print(i,' и ',j)
else:
    print('Знакомить не буду, кто-то может остаться без пары')







# In[65]:


# Альтернативный вариант решения задачи № 2.

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys.sort()
girls.sort()

if len(boys) == len(girls):
    print('Идеальные пары:')
    for i in range(len(boys)):
        print(boys[i], 'и', girls[i])
else:
    print('Знакомить не буду, кто-то может остаться без пары')


# Задача 3. У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах за недельный период по странам. Необходимо написать код, который рассчитает среднюю температуру за неделю в Цельсиях для каждой страны.

# In[68]:


countries_temperature = [
 ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
 ['Germany', [57.2, 55.4, 59, 59, 53.6, 55.4, 57.2]],
 ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
 ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4, 51.8]],
]

import numpy
print ('Средняя температура в Цельсиях за неделю для каждой страны из списка:')
for i in range(len(countries_temperature)):
        print(countries_temperature[i][0], '-', round(numpy.mean(countries_temperature[i][1])-32,2))


# Задача 4. Дан поток логов по количеству просмотренных страниц для каждого пользователя. Список отсортирован по ID пользователя. Вам необходимо написать алгоритм, который считает среднее значение просмотров на пользователя. Т. е. надо посчитать отношение суммы всех просмотров к количеству уникальных пользователей.

# In[1]:


stream = [
    '2018-01-01,user1,3',
    '2018-01-07,user1,4',
    '2018-03-29,user1,1',
    '2018-04-04,user1,13',
    '2018-01-05,user2,7',
    '2018-06-14,user3,4',
    '2018-07-02,user3,10',
    '2018-03-21,user4,19',
    '2018-03-22,user4,4',
    '2018-04-22,user4,8',
    '2018-05-03,user4,9',
    '2018-05-11,user4,11',
]


a = ','.join(stream)
stream_ = a.split(',')

def super_split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

stream_ = list(super_split(stream_,len(stream)))

user_dict = []
count_brows = 0

for i in range(len(stream_)):    
    
    count_brows = count_brows + int(stream_[i][2])  
   
    if stream_[i][1] not in user_dict != True:
        user_dict.append(str(stream_[i][1]))
    else:
        continue

print('Среднее кол-во просмотров на одного пользователя составляет:',count_brows/len(user_dict))


# Задача 5. Дана статистика рекламных кампаний по дням. Напишите алгоритм, который по паре дата-кампания ищет значение численного столбца. Т. е. для даты '2018-01-01' и 'google' нужно получить число 25. Считайте, что все комбинации дата-кампания уникальны.

# In[2]:


stats = [
    ['2018-01-01', 'google', 25],
    ['2018-01-01', 'yandex', 65],
    ['2018-01-01', 'market', 89],
    ['2018-01-02', 'google', 574],
    ['2018-01-02', 'yandex', 249],
    ['2018-01-02', 'market', 994],
    ['2018-01-03', 'google', 1843],
    ['2018-01-03', 'yandex', 1327],
    ['2018-01-03', 'market', 1764],
]

input_date = input('Введите дату в формате гггг-мм-дд: ')
company_name = input('Введите название компании: ')

for i in range(len(stats)):
    if input_date == stats[i][0] and company_name == stats[i][1]:
        print(stats[i][2])
        break
    else:
        continue


# Задача 6. Напишите код, который будет вычислять сумму элементов на диагонали. Т. е. 13+32+23+35.
# Список может быть любой длины, но всегда является "квадратным" (количество элементов во вложенных списках равно их количеству).
# 

# In[3]:


data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35]
]

a = 0
for i in range(len(data)):
        a = a + int(data[i][i])
print(a)


# In[ ]:




