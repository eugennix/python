def lagranj(n):
    # up to 20-30 digit n
    r1 = int(n**0.5)

    # case 1 sq
    if r1**2 == n:
        return [r1]

    # case more sq
    for q1 in range(r1, 0, -1):
        s1 = q1**2
        if s1 > n:
            continue

        r2 = int((n-s1)**0.5)
        for q2 in range(r2, 0, -1):
            s2 = s1 + q2**2
            if s2 >= n:
                if s2 > n:
                    continue
                else:
                    return [q2, q1]                

            r3 = int((n-s2)**0.5)
            for q3 in range(r3, 0, -1):
                s3 = s2 + q3**2
                if s3 == n:
                    return [q3, q2, q1]

                q4 = int((n-s3)**0.5)
                if s3 + q4**2 == n:
                    return [q4, q3, q2, q1]

    # something wrong - bad algorithm
    return []
import time as t
while True:
    n = int(input())
    st = t.time()
    if not n:
        break
    print(*lagranj(n))
    print(f'{t.time()-st:f} sec')

