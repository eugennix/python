a, b, c = [float(input()) for _ in range(3)]
zero = 1.0e-8


def trunc0(n):
    sn = str(n).split('.')
    if len(sn) == 2 and sn[1] == '0':
        return int(sn[0])
    return n


def ax2bxc0(a, b, c):
    if abs(a) < zero:
        if abs(b) < zero:
            if abs(c) < zero:
                return [3]
            else:
                return [0]
        else:
            return [1, trunc0(-c / b)]

    d = b * b - 4 * a * c
    if d >= 0:
        x1 = (-b - (d)**0.5) / (2 * a)
        x2 = (-b + (d)**0.5) / (2 * a)
        if x1 > x2:
            x1, x2 = x2, x1
        if (x2 - x1) < zero:
            x = (x2 + x1) / 2
            return [1, trunc0(x)]
        else:
            return [2, trunc0(x1), trunc0(x2)]
    else:
        return [0]

print(*ax2bxc0(a, b, c))
