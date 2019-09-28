'''
в первой строке записано количество строк в тексте, а затем сами строки.
 Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
 Слова должны быть отсортированы по убыванию их количества появления в тексте,
 а при одинаковой частоте появления — в лексикографическом порядке.

Указание. После того, как вы создадите словарь всех слов, вам захочется
 отсортировать его по частоте встречаемости слова. Желаемого можно добиться,
 если создать список, элементами которого будут кортежи из двух элементов:
 частота встречаемости слова и само слово. Например,
 [(2, 'hi'), (1, 'what'), (3, 'is')].
 Тогда стандартная сортировка будет сортировать список кортежей,
 при этом кортежи сравниваются по первому элементу, а если они равны
 — то по второму. Это почти то, что требуется в задаче.
'''

from collections import Counter
n, count = int(input()), Counter()
for _ in range(n):
    line = input().replace('.', ' ').replace(',', ' ').replace('!', ' ')
    print(line)
    count.update(line.split())
# одной строкой
# [count.update(x) for x in (input().split() for _ in range(n))]
print(count)

result = sorted((-cou, w) for w, cou in count.items())
print(result)

print(*[w for c, w in result], sep='\n')

''' input
9
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme


output ->
'''