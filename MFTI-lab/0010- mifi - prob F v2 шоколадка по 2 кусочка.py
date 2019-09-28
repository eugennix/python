# n1 2 3 4
#  0 3 6 9
#  1 4 7 10
#  2 5 8 11 ...

# 2 -> 3
# 4 -> 11
# 10 -> 571
# 1 -> 0
# 117 -> 0
# 10000 -> .....

def chocko_3xN_permutation(n):
    """
    :param n: размер шоколадки
    :return:    сколькими способами можно разделить шоколадку 3xn
                по доминошкам 2х1
                без остатков маленьких кусочков
    """
    # для нечётного n плитка не делится по 2 кусочка
    if n % 2 or n < 1:
        return 0
    #
    elif n == 2:
        return 3
    else:
        # для n - 6, 8, добавляем по 2 ряда -
        # *3 перестановок с n-2
        # +2 перестановки с n-4, когда добавляемые ряды заходят в существующие
        total_m2, total_m4 = 11, 3
        count = 4
        while count < n:
            count += 2
            # правильная формула
            # new_total = total_m2 * 3 + 2 * total_m4

            # формула в тестах
            new_total = total_m2 * 4 - total_m4
            total_m2, total_m4 = new_total, total_m2
        return total_m2

def chocko_3xN_per_1(n):
    """
    :param n: размер шоколадки
    :return:    сколькими способами можно разделить шоколадку 3xn
                по доминошкам 2х1
                без остатков маленьких кусочков
    # https://www.algorithmist.com/index.php/UVa_10918
    # f(0)=1, f(1)=0, g(0)=0, g(1)=1.
    # f(n)=f(n-2)+2g(n-1)
    # g(n)=f(n-1)+g(n-2)

    """
    # для нечётного n плитка не делится по 2 кусочка
    if n % 2 or n < 1:
        return 0
    else:
        f_m1, f_m2 = 1, 0
        g_m1, g_m2 = 1, 0
        count = 0
        while count < n:
            count += 1
            # правильная формула
            # new_total = total_m2 * 3 + 2 * total_m4
            f_n = f_m2 + 2 * g_m1
            g_n = f_m1 + g_m2
            f_m1, f_m2 = f_n, f_m1
            g_m1, g_m2 = g_n, g_m1

        return f_n



n = int(input())
print(chocko_3xN_permutation(n))
print(chocko_3xN_per_1(n))


