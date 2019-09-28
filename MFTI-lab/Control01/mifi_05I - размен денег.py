'''
Написать функцию make_exchange(money, coins),
 которая принимает сумму денег (целое число)
и массив номиналов разменных монет (целых чисел) (возможно пустой)
и возвращает количество способов произвести размен.
Считаем, что разменных монет бесконечное множество.

# Формат выходных данных
Число способов произвести размен. Способы 1+2 и 2+1 считаем тождественными.
'''


def make_exchange(money: int, coins: list) -> int:
    F = [0] * (money + 1)
    for i in coins:
        if i <= money:
            F[i] = 1
    for i in range(1, money + 1):
        for coin in coins:
            if i - coin >= 0 and F[i - coin]:
                F[i] += F[i - coin]
                print(i, '-', coin, 'from ', i - coin, '>', F[i])
        print(f'total {i} == {F[i]}')
    return F[-1]


x = make_exchange(10, [5, 2, 3])
print(x)
#