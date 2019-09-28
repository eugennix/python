n = int(input())
paints = [tuple([int(input()), int(input()), int(input())]) for _ in range(n)]
m = int(input())
reqsts = [int(input()) for _ in range(m)]
answrs = []

for rqst in reqsts:
    found_color = 0
    for left, right, color in reversed(paints):
        if left <= rqst <= right:
            found_color = color
            break
    answrs.append(found_color)

print(*answrs)
