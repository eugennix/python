
n, m = map(int, input().split())
matrix = [input().split() for i in range(n)]

print(*[' '.join(x) for x in matrix], sep='\n')
matrix = [*zip(*matrix)]

print(*[' '.join(x) for x in matrix], sep='\n')