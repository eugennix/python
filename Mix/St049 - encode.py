s = 'qqaaabccccCCaBsssssdddddxxw'
# в конец добавлен фиктивный символ ~~~


def base_RLE_encode(txt):
    result, txt, pred, count = '', txt + '~~~', txt[0], 0
    for x in txt:
        if x == pred:
            count += 1
        else:
            result += str(count) * (count > 1) + pred
            pred, count = x, 1
    return result


print(baseRLEencode(s))
