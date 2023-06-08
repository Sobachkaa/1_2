# Для перевода DataFrame в one hot вид без использования функции 
# get_dummies
#  можно использовать метод 
# pd.get_dummies()
#  с параметром 
# drop_first=True
# , который удаляет первый столбец, который создаётся при использовании one hot encoding.
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot_data = pd.get_dummies(data['whoAmI'], drop_first=True)

print(one_hot_data)