'''
for tests
'''
txt = []
with open('dataset_24465_4.txt') as infi:
    for l in infi:
        txt.append(l)

with open('outfile.txt', 'w') as outfi:
    for l in txt[::-1]:
        outfi.write(l)

lines = open("input.txt").readlines()
with open("output.txt", "w") as out:
    out.writelines(reversed(lines))

