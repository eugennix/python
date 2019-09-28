'''
 в первой строке задано число строк, далее идут сами строки.
 Выведите слово, которое в этом тексте встречается чаще всего.
 Если таких несколько - которое меньше в лексикографическом порядке.
'''

from collections import Counter
n, count = int(input()), Counter()
[count.update(x) for x in (input().split(' ') for _ in range(n))]
# в порядке убывания счётчика
most_comm = count.most_common()
print(most_comm)
# фильтруем с максимальным счётчиком
mc_high = [x for x, c in most_comm if c == most_comm[0][1]]
print(mc_high)
print(sorted(mc_high)[0])

''' data
3
qw qw qw e
sd sd sd
re re re

output ->
'''