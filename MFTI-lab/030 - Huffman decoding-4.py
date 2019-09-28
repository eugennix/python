# словарём
def Huffman_decode(bit_seq: str, d: dict) -> str:
    decode_table = dict((code, sym) for sym, code in code_table.items())
    result = []
    part_bits = ''
    for bit in bit_seq:
        part_bits += bit
        if part_bits in decode_table:
            result.append(decode_table[part_bits])
            part_bits = ''
    return ''.join(result)
difsyms, codelen = map(int, input().split())
code_table = dict(input().split(': ') for _ in range(difsyms))
to_decode = input()

import time
st = time.time()
print(Huffman_decode(to_decode, code_table))
print(f'time {time.time()-st:6f}')
