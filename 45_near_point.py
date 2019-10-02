''' https://www.coursera.org
/learn/python-osnovy-programmirovaniya/programming/Hs8PB/grazhdanskaia-oborona
'''
input()
n_points = sorted(enumerate(map(int, input().split())), key=lambda x: x[1])
input()
m_points = sorted(enumerate(map(int, input().split())), key=lambda x: x[1])
result = [0] * len(n_points)

# добавляем фиктивное очень далёкое бомбоубежище, чтобы вообще не париться
# с выходом за границу массива - оно всегда проиграет в любом сравнении
mi = 0
m_points.append((None, -2**100))

for nomer, coord in n_points:
    while abs(m_points[mi][1] - coord) > abs(m_points[mi+1][1] - coord):
        mi += 1
    result[nomer] = m_points[mi][0] + 1

print(*result)
