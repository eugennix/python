a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())


def arrange(a, b, c):
    '''
    :return: a <= b <= c
    '''
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return a, b, c

a1, b1, c1 = arrange(a1, b1, c1)
a2, b2, c2 = arrange(a2, b2, c2)
if a1 == a2 and b1 == b2 and c1 == c2:
    print('Boxes are equal')
elif a1 <= a2 and b1 <= b2 and c1 <= c2:
    print('The first box is smaller than the second one')
elif a2 <= a1 and b2 <= b1 and c2 <= c1:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
