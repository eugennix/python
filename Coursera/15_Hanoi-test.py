def hanoi(x_from, x_to, n):
    if n == 1:
        print(n, x_from, x_to)
        return

    # вспомогательный столбик - иной чем x_from и x_to
    x_other = 6 - x_from - x_to

    # переносим n-1 на вспомогательный
    hanoi(x_from, x_other, n-1)

    # переносим нижний блин на нужный
    print(n, x_from, x_to)

    # переносим с третьего на нужный
    hanoi(x_other, x_to, n-1)


hanoi(1, 3, int(input()))
