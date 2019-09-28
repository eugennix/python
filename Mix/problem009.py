""" A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5***2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
sum_rq = 1000
for a in range(1, sum_rq//3+1):
    for b in range(a+1, (sum_rq - a)//2 + 1):
        c =  sum_rq - a - b
        if c == b: continue
        if a*a + b*b == c*c:
            print (">" + str(a) + " * " + str(b) + " * " + str(c) + " = " + str(a*b*c))

