from collections import Counter
difsyms, codelen = map(int, input().split())
code_table = dict(input().split(': ') for _ in range(difsyms))
to_decode = input()

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


def Huffman_decode(coded: str, d: dict) -> str:
    # decode_table = dict((code, sym) for sym, code in code_table.items())
    # print(decode_table, '\n', d)

    # строю дерево для декодирования
    root = Tree()
    for sym, code in d.items():
        pointer = root
        for bit in code:
            if bit == '0':
                if pointer.left is None:
                    pointer.left = Tree()
                pointer = pointer.left
            else:
                if pointer.right is None:
                    pointer.right = Tree()
                pointer = pointer.right
        pointer.data = sym

    result = []
    pointer = root
    for bit in coded:
        if bit == '0':
            pointer = pointer.left
        else:
            pointer = pointer.right
        if pointer.data is not None:
            result.append(pointer.data)
            pointer = root

    return ''.join(result)


decoded_str = Huffman_decode(to_decode, code_table)
print(decoded_str)

'''

'''