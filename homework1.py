import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

#3. Создание массива случайных чисел
# array_size = 10
# random_array = [random.randint(1, 100) for _ in range(array_size)]
#print(f"Массив случайных чисел: {random_array}")
#print(sum(random_array))

# def list_sum(*args):
#     s = sum(*args)
#     return s

#print(list_sum(random_array))

"""
4. Создание массива из 20 случайных чисел и вычсление среднего
значения из них с помощью numpy
"""

#print(np.random.randint(1, 100, size=20))

# def get_random_average(min, max, count):
#     l = np.random.randint(min, max, count)
#     avg = np.mean(l)
#     return f'{l=}, {avg=}'

#print(get_random_average(1, 100, 20))

"""
Пример программы на Python с использованием библиотеки Pandas 
для чтения CSV-файла и печати первых пяти строк: 
"""

# Укажите путь к файлу CSV
#csv_file_path = "example_5kb.csv"

# Чтение CSV-файла с помощью Pandas
#data = pd.read_csv(csv_file_path)

# Печать первых 5 строк
#print(data.head(5))

# df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
#                    'B': [5, 6, 7, 8, 9],
#                    'C': ['a', 'b', 'c', 'd', 'e']})
# df = df.replace(0, 8)
# print(df)

# x, y = [], []
# with open('excelweek2017_2018.csv', 'r', encoding='UTF-8') as csv_file:
#     f_str = csv_file.read().replace(',', '.')
#     f_str = f_str.replace('\"', '')
    # l = []
    # for line in f_str:
    #     l.append(line.split('\n'))
    # print(l)
    # row = f_str.split('\n')
    # l = []
    # for el in row:
    #     l.append(el.split(';'))
    # del(l[-1])
    # col = l.pop(0)
    # df_value = f'({l}, columns={col})'

#     #f_str = f_str.replace(';', ',')
#     #f_str.split('\n')
#     for line in f_str:

    #     print(list(line))
    #data = pd.DataFrame(f_str)
# with open('test.csv', 'w', encoding='UTF-8') as fl:
#     fl.write(f_str)

# with open('test.csv', 'r', encoding='UTF-8') as file:
#     data = pd.read_csv(file)
#     grouped_data = data.groupby(['IDLogin' , 'DATE'])['Sum'].sum()
#     print(grouped_data)

with open('test1.csv', 'r', encoding='UTF-8') as file:
#     #fl.write(f_str)
#     # csv_file.seek(0)
#     # csv_file.truncate()
#     # csv_file.write(f_str)
#     #print(f_str)
     data = pd.read_csv(file, delimiter=';')
#     # data = data.replace(',', '.')
     dataId = data.IDLogin# один столбец
     dataId = dataId.drop_duplicates()# удаляем дубликаты
     data_val = dataId.values
     #print(data_val)# итератор по id
for id in data_val:# фильтруем по мерчанту
     cond = data[data['IDLogin'] == id]
     group_date = cond.groupby(['DATE'])['DATE'].max()
     #print(group_date)
     group_cond = cond.groupby(['DATE'])['Sum'].sum()
     #print(group_cond)
     X, Y = [], []
     for date in group_date:
     # #      print()
            X.append(date)
     for rows in group_cond:
     # #      print(rows)
            Y.append(rows)
     #print(X, Y)
     #group_cond.plot(kind='barh', fontsize=4)
     plt.plot(X, Y)
     group_cond.plot.bar()
     #plt.plot(kind='bar')
     #plt.legend(id)
plt.title('billing')
plt.xlabel('Дата')
plt.ylabel('Траффик')
plt.show()
     #print(group_cond)
     #cond = data.query('IDLogin' == id)# фильтруем по столбцу
     #print(id)
     #group_cond = cond.groupby(['DATE'])['Sum'].sum()
     #print(group_cond)
     # for idx_row, row in dataId.iterrows():
     # #     ch = data.query('IDLogin == row')
     #      print(row)



    #print(data['IDLogin'].count())
    # group_id = data.groupby(['IDLogin'])['IDLogin'].count()
    # print(group_id)
    # grouped_data = data.groupby(['IDLogin' , 'DATE'])['Sum'].sum()
    # print(grouped_data)

# date = []
# idLogin = []
# amount = []
# for row in grouped_data:
#     print(row)

#     plots = csv.reader(csv_file, delimiter=';')
#     for row in plots:
#         x.append(row[1])
#         y.append(row[2])
#
# plt.plot(x, y)
# plt.title('billing')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

#df.loc[2:4, 'A'] = df.loc[2:4, 'A'].replace({10: 'десять'})

# s = pd.Series([1, 2, 3, 4, 5])
# s = s.replace(1, 5)
# print(s)


#df = pd.DataFrame(df_value)
#
# print(df)

# with open('test1.csv', 'r', encoding='UTF-8') as file:
#     data = pd.read_csv(file)
#     #print(data)
#     grouped_data = data.groupby(['IDLogin' , 'DATE'])['Sum'].sum()
#     print(grouped_data)