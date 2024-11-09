import pandas as pd
import matplotlib.pyplot as plt


arr, el, col = [], [], ['Дата']

with open('test.csv', 'r', encoding='UTF-8') as file:# открываем файл на чтение
     data = pd.read_csv(file, delimiter=';')# считываем данные из формата csv
     dataId = data.IDLogin# получаем один столбец - мерчант
     dataId = dataId.drop_duplicates()# удаляем дубликаты
     data_val = dataId.values# получаем список мерчантов
     for val in range(len(data_val)):# цикл по мерчантам
         el.append(0)# добавляем нулевые значения для заполнения пустых значений из csv
     dataDate = data.DATE # получаем один столбец - даты
     dataDate = dataDate.drop_duplicates()# удаляем дубликаты дат для создания списка оси Х
     dataDate = sorted(dataDate)#получили отсортированный список дат для оси Х
     for dat in range(len(dataDate)):# добавляем в arr даты (каждая в виде списка)
         arr.append([dataDate[dat]] + el)# для корректного отображения графиков заполняем пустые даты по каждому мерчанту
     count = 0 #счетчик цикла
for id in data_val:# цикл по мерчанту
     col.append(id)# добавляем в список мерчанта
     condition = data[data['IDLogin'] == id]# производим подготовку данных для графика по каждому мерчанту
     group_date = condition.groupby(['DATE'])['DATE'].max() # группируем даты мерчанта
     date_id = group_date.values# получаем список дат
     group_cond = condition.groupby(['DATE'])['Sum'].sum() #группируем суммы биллинга мерчанта по датам
     sum_id = group_cond.values# получаем список сумм
     count += 1
     for date in arr:# проходим циклом по списку для графика
         for d in range(len(date_id)):# внутренний цикл по списку дат мерчанта
             if date_id[d] == date[0]: # если значения дат совпали:
                 date[count] = float(sum_id[d])# меняем значение списка для графика (по умолчанию - 0) на сумму по дате мерчанта из csv
                 break# если даты совпали и сумма заменена - выходим из цикла, чтобы не делать лишнюю работу

df = pd.DataFrame(arr, columns=col)#создаем экземпляр класса DataFram с массивом для графика и списка мерчантов для графика
df.plot(x="Дата", y=data_val)# настройка осей Х, Y, типа графика, формата окна вывода
plt.xticks(rotation=30)# для удобства подписи оси Х датами делаем под наклоном 30%
plt.title('billing')# заголовок графика
plt.xlabel('Дата')# имя оси Х
plt.ylabel('Траффик') # имя оси Y
plt.show()# вывод на экран

