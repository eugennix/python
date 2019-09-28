def toStr(x):
    return "".join(str(i) for i in x)

def create_phone_number1(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

def create_phone_numberMY(n):
    return "({}) {}-{}".format(toStr(n[:3]), toStr(n[3:6]), toStr(n[6:]))

def create_phone_numberMY2(n):
    n = ''.join(map(str, n))
    return "({}) {}-{}".format(n[:3], n[3:6], n[6:])

# best
def create_phone_number(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
