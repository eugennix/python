"""def find_missing_letter(ch):
    for i in range(len(ch) - 1):
        if ord(ch[i]) + 1 != ord(ch[i + 1]):
            return chr(ord(ch[i]) + 1)
"""
def find_missing_letter(ch):
    for c1, c2 in zip(ch[:-1], ch[1:]):
        if ord(c1) + 1 != ord(c2):
            return chr(ord(c1) + 1)


print(find_missing_letter(['a','b','c','d','f']))



i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1
print(i)

print("=====================")
a, b, c, d = 7, 10, 5, 6
# a, b, c, d = (int(input()) for x in range(4))
print('', *range(c,d+1), sep='\t')
for x in range(a, b+1):
    print(x, *[y*x for y in range(c, d+1)], sep='\t')

print("=====================")

print('', *range(c, d+1), sep='\t')
[ print(*[i, *range(i*c, i*d+1, i)], sep='\t') for i in range(a, b+1) ]

print("=====================")
"""
#a, b = int(input()), int(input()), 0
a, b, su = int(input()), int(input()), [x for x in range(a, b+1) if not x % 3]
su = [x for x in range(a, b+1) if not x % 3]
print(sum(su) / len(su))

x = [x for x in range(int(input()), int(input()) + 1) if not x % 3]
print(sum(x) / len(x))
"""
print("=====================")
"""
for i in range(a, b+1):
    if not i % 3:
        su += i
        c += 1
print(su/c)"""


s = 'abcdefghijk'
# print(s[3:6])
# print(s[:6])
# print(s[3:])
# print(s[::-1])
# print(s[-3:])
# print(s[:-6])
# print(s[-1:-10:-2])
