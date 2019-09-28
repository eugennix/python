import json

chlds, prnts = dict(), dict()

def visit_prnts(chi, prn):
    # print(f'{chi} visited {prn}')
    chlds[prn].add(chi)
    if prnts.get(prn):
        for x in prnts[prn]:
            visit_prnts(chi, x)

# classes_j = input()
classes_j = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'
classes_j = '[{"name": "G", "parents": ["F"]}, {"name": "A", "parents": []}, {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents": ["B", "C"]}, {"name": "E", "parents": ["D"]}, {"name": "F", "parents": ["D"]}, {"name": "X", "parents": []}, {"name": "Y", "parents": ["X", "A"]}, {"name": "Z", "parents": ["X"]}, {"name": "V", "parents": ["Z", "Y"]}, {"name": "W", "parents": ["V"]}]'

classes = json.loads(classes_j)

for cl_d in classes:
    cl_name = cl_d['name']
    prnts[cl_name] = cl_d['parents']
    chlds[cl_name] = set()

for cl_d in classes:
    cl_name = cl_d['name']
    visit_prnts(cl_name, cl_name)

print(*[cl+' : '+str(len(chlds)) for cl, chlds in sorted(chlds.items())], sep='\n')

print(classes)
print(prnts)