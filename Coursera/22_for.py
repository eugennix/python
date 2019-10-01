l = list(map(int, input().split()))
new_index, new_elem = map(int, input().split())
l.append(0)
for i in range(len(l)-1, new_index, -1):
    l[i] = l[i-1]
l[new_index] = new_elem
print(*l)
