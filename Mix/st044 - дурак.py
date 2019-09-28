'''
A durak deck contains 36 cards. Each card has a suit of either
 clubs, diamonds, hearts, or spades (denoted C, D, H, S).
 Each card also has a value of either 6 through 10, jack, queen, king, or ace
 (denoted 6, 7, 8, 9, 10, J, Q, K, A).
 For scoring purposes card values are ordered as above,
 with 6 having the lowest and ace the highest value.

Напишите программу, которая определяет, бьёт ли одна карта другую.
Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
Если карты разных мастей и нет козырных, то никто не побеждает.

Формат ввода:
На первой строке через пробел указываются две карты в формате <значение><масть>,
 а на следующей строке указывается козырная масть.

Формат вывода:
First, если первая карта бьёт вторую,
Second, если вторая карта бьёт первую,
Error, если ни одна из карт не может побить другую.

AH JH
D
'''
c1, c2 = input().split()
trump = input()
crd_v = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

first_win, error = False, False

if c1[-1] == c2[-1]:
    first_win = crd_v[c1[:-1]] > crd_v[c2[:-1]]
    error = crd_v[c1[:-1]] == crd_v[c2[:-1]]
elif c1[-1] == trump:
    first_win = True
elif c2[-1] != trump:
    error = True

if error:
    print('Error')
elif first_win:
    print('First')
else:
    print('Second')

print('Error' if error else 'First'*first_win + 'Second'*(not first_win))


# Хорошо сравнивать tuple.
(c1, c2), m = input().replace('10', 'T', 2).split(), input()

r1 = (c1[1] == m, '6789TJQKA'.find(c1[0]) * (c1[1] == c2[1]))
r2 = (c2[1] == m, '6789TJQKA'.find(c2[0]) * (c1[1] == c2[1]))

ans = 0 if r1 > r2 else 1 if r1 < r2 else 2
print(['First', 'Second', 'Error'][ans])

max