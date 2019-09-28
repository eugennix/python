'''
В первой строке дано количество записей.
Далее, каждая запись содержит фамилию кандидата и число голосов,
отданных за него в одном из штатов. Подведите итоги выборов:
для каждого из участника голосования определите число
отданных за него голосов. Участников нужно выводить в алфавитном порядке.
'''

# v2
from collections import Counter
n, count = int(input()), Counter()
[count.update({n: int(v)}) for n, v in (input().split(' ') for _ in range(n))]

print(*[f"{n} {v}" for n, v in sorted(count.items())], sep='\n')


''' v1
from collections import Counter
n, count = int(input()), Counter()
votes = [{n: int(v)} for n, v in (input().split(' ') for _ in range(n))]
count.update(*votes)

print(*["{} {}".format(n, v) for n, v in sorted(count.items())], sep='\n')
'''

''' data
13
McCain 10
McCain 3
Obama 19
Obama 2
McCain 7
McCain 2
Obama 6
Obama 10
McCain 11
McCain 5
Obama 3
Obama 12
McCain 13


output ->
McCain 51
Obama 52
'''