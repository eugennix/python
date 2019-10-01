n = int(input())

print(' '.join(['+___' for i in range(1, n+1)]))
print(' '.join([('|' + str(i) + ' /') for i in range(1, n+1)]))
print(' '.join(['|__\\' for i in range(1, n+1)]))
print(' '.join(['|   ' for i in range(1, n+1)]))
