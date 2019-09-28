from collections import Counter

def Huffman(to_code:str) -> dict:
    c = Counter(to_code)
    freq = [(su, sym) for sym, su in c.items()]
    freq.sort(reverse=True)
    d = dict()
    if len(freq) == 1:
        d[freq[0][1]] = '0'
    else:
        while len(freq) >= 2:
            # получить элементы с самой малой частотой
            node1, node2 = freq.pop(), freq.pop()
            # к коду худшего добавляю вначале '0'
            # ко второму  - '1' .
            # Для всех символов, входящие в эти элементы
            for sym in node1[1]:
                d[sym] = '0' + d.get(sym, '')
            for sym in node2[1]:
                d[sym] = '1' + d.get(sym, '')
            # склеиваю строки этих элементов
            sym_new = node1[1] + node2[1]
            # суммирую их частоты
            freq_new = node1[0] + node2[0]
            # новый элемент == сумма частот нижележащих символов
            # sym_new = все эти символы одной строкой
            freq.append((freq_new, sym_new))
            # упорядочить
            freq.sort(reverse=True)
    return d


class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

class Huffman_Tree (Tree):

    def new_key(self, sym, bitcode):
        pointer = self
        for bit in bitcode:
            if bit == '0':
                if pointer.left is None:
                    pointer.left = Tree()
                pointer = pointer.left
            else:
                if pointer.right is None:
                    pointer.right = Tree()
                pointer = pointer.right
        pointer.data = sym

    def decode(self, bitseq):
        result = []
        pointer = self
        for bit in bitseq:
            pointer = (pointer.left, pointer.right)[bit == '1']
            if pointer.data is not None:
                result.append(pointer.data)
                pointer = self
        return ''.join(result)

def Huffman_decode(coded: str, d: dict) -> str:
    root = Huffman_Tree()
    for sym, code in d.items():
        root.new_key(sym, code)
    return root.decode(coded)

difsyms, codelen = map(int, input().split())
code_table = dict(input().split(': ') for _ in range(difsyms))
to_decode = input()

import time
st = time.time()
print(Huffman_decode(to_decode, code_table))
print(f'{time.time()-st:6f}')
