import sys
import re
''' v1
patt = r'.*?(cat).*?(cat).*?'
reLst = []
for ln in sys.stdin:
    ln = ln.rstrip()
    fnd = re.search(patt, ln)
    if fnd is not None:
        reLst.append(ln)
print(*reLst, sep='\n')
'''
'''
patt = r'.*?(cat).*?(cat).*?'
for ln in sys.stdin:
    ln = ln.rstrip()
    if re.search(patt, ln):
        print(ln)
'''

patt = r'.*?(cat).*?(cat).*?'
print(*[ln.strip() for ln in sys.stdin if re.search(patt, ln)], sep='\n')
