import csv

with open('Crimes.csv') as inf:
    crimes = [x for x in csv.reader(inf)]

print('Записей = ', len(crimes))
print(*crimes[0:5], sep='\n')

def get_year(datex):
    return datex[6:10]

cr_2015 = dict()
for ID, CaseNumber, Date, Block, IUCR, PrimaryType, \
        Description, LocationDescription, Arrest, Domestic, \
        Beat, District, Ward, CommunityArea, FBICode in crimes:

        if get_year(Date) == '2015':
            cr_2015[PrimaryType] = cr_2015.get(PrimaryType, 0) + 1
max_crime = max(cr_2015.items(), key=lambda kv: kv[1])
print(max_crime[0])
# print(*sorted(cr_2015.items(), key=lambda kv: kv[1], reverse=1), sep='\n')


'''
1) csv читаем с помощью DictReader, чтобы не нужно было открывать файл
и выяснять каким по счёту идёт нужный столбец.
Сказали есть столбец 'Primary Type', значит и будем его читать,
вся остальная структура файла не интересует.

2) Создаём список всех 'Primary Type' в 2015 году 
(по хорошему, нужно дату парсить, но не хотелось с форматами возиться,
 поэтому просто if '2015' in row['Date']

3) Из списка делаем множество, тогда остаются только по одному вхождению каждого
 'Primary Type', а максимальное количество среди них ищем с помощью лямбда-функции,
  используя count(x) в исходном списке
В ответ выводим само преступление и количество случаев в 2015 году.

import csv
crimes = [row['Primary Type'] for row in csv.DictReader(open("Crimes.csv")) if '2015' in row['Date']]
crime = max(set(crimes), key=lambda x: crimes.count(x))
print(crime, crimes.count(crime))
'''