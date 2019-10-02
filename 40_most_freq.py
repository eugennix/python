""" Дан список. Не изменяя его и не используя дополнительные списки,
 определите, какое число в этом списке встречается чаще всего
"""

li = list(map(int, input().split()))
ans, max_freq = None, 0
for elem in li:
    if li.count(elem) > max_freq:
        max_freq = li.count(elem)
        ans = elem

print(ans)
