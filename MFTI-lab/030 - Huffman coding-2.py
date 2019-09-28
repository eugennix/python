from collections import Counter

to_code = input()

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

d = Huffman(to_code)
c = Counter(to_code)

# total_code_len = sum([len(d[sym])*count for sym, count in c.items()])

coded = ''.join(d[sym] for sym in to_code)
print(len(c), len(coded))

codes = sorted(d.items(), key= lambda x: len(x[1]))
print(*[f'{sym}: {code}' for sym, code in codes], sep='\n')

print(coded)



