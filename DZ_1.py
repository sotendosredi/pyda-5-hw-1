#!/usr/bin/env python
# coding: utf-8

# In[4]:


long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
len (long_phrase) > len (short_phrase)


# In[12]:


file_w = 6432623123
a = 2**20
print (file_w/a)


# In[15]:


month = input("Введите месяц рождения: ")
month = month.lower()
date = int(input("Введите день рождения: "))

if month == 'март':
  sign = 'овен' if (date >= 21) else 'рыбы'
elif month == 'апрель':
  sign = 'телец' if (date >= 21) else 'овен'
elif month == 'май':
  sign = 'близнецы' if (date >= 22) else 'телец'
elif month == 'июнь':
  sign = 'рак' if (date >= 22) else 'близнецы'
elif month == 'июль':
  sign = 'лев' if (date >= 23) else 'рак'
elif month == 'август':
  sign = 'дева' if (date >= 24) else 'лев'
elif month == 'сентябрь':
  sign = 'весы' if (date >= 24) else 'дева'
elif month == 'октябрь':
  sign = 'скорпион' if (date >= 24) else 'весы'
elif month == 'ноябрь':
  sign = 'стрелец' if (date >= 23) else 'скорпион'
elif month == 'декабрь':
  sign = 'козерог' if (date >= 23) else 'стрелец'
elif month == 'январь':
  sign = 'водолей' if (date >= 21) else 'козерог'
elif month == 'февраль':
  sign = 'рыбы' if (date >= 21) else 'водолей'
print ("Ваш знак зодиака - " + sign);


# In[21]:


s = int (input ("Введите заработанную плату в месяц: "))
i = int (input ("Введите сколько процентов уходит на ипотеку: "))
l = int (input ("Введите сколько процентов уходит на жизнь: "))
p = s/2*int (input("Введите количество премий за год: "))
print ('На ипотеку было потрачено: ', s*i/100*12, 'рублей. Было накоплено: ', (s-(s*i/100)-(s*l/100))*12+p, 'рублей.')


# In[ ]:




