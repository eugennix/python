from xml.etree import ElementTree
from sys import stdin
'''
Введем понятие ценности для кубиков. Самый верхний кубик,
 соответствующий корню XML документа имеет ценность 1.
  Кубики, расположенные прямо под ним, имеют ценность 2.
   Кубики, расположенные прямо под нижележащими кубиками,
    имеют ценность 3. И т. д.
Ценность цвета равна сумме ценностей всех кубиков этого цвета.
Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
'''
test = '''<cube color="blue">
    <cube color="red">
		<cube color="green">
        </cube>
    </cube>
    <cube color="red">
    </cube>
</cube>

'''

def evaluate_node(node, val):
    color = node.attrib["color"]
    print(color)
    colors_val[color] = colors_val.get(color, 0) + val
    for child in node:
        evaluate_node(child, val + 1)
    return


colors_val = {'red': 0, 'green': 0, 'blue': 0}
# tree = ElementTree.parse(stdin)
# tree = ElementTree.ElementTree(ElementTree.fromstring(test))
tree = ElementTree.parse('dataset.xml')


evaluate_node(tree.getroot(), 1)
print(*[f'{v} - {k}' for k, v in colors_val.items()], sep='\n')



new_cube = ElementTree.SubElement(tree.getroot(), "cube")
new_cube.attrib['color'] = 'black'
tree.write('dataset.xml')
'''
from xml.etree import ElementTree
colors = {"red": 0, "green": 0, "blue": 0}  # словарь ключ=цвет

def finder(root, count=1):
    colors[root.attrib["color"]] += count  # нашли цвет добавили к счётчику

    [finder(child, count + 1) for child in root]  # поиск во вложениях        

finder(ElementTree.fromstring(input()))  # считываем xml-строку

print(colors["red"], colors["green"], colors["blue"])  # выдаём ответ

'''