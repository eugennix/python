numerics = lambda n: [d for d in str(n)]

def kaprekar_check(n):
    ln = len(str(n))
    return False if ln not in (3, 4, 6) or len(set(numerics(n))) == 1 or n == 10**(ln - 1) else True

def kaprekar_step(L):
    Ls = sorted(L)
    return str(int(''.join(d for d in Ls[::-1])) - int(''.join(d for d in Ls))).zfill(len(L))

def kaprekar_loop(n):
    if not kaprekar_check(n):
        print(f'Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара')
    else:
        n = str(n)
        print(n)
        d = {n}
        while n not in ('495', '6174', '549945', '631764'):
            n = kaprekar_step(numerics(n))
            if n in d:
                print(f'Следующее число - {n}, кажется процесс зациклился...')
                break
            d.add(n)
            print(n)

kaprekar_loop(211111)

