def rot13_1(m):
    def r13(s):
        snew = chr(ord(s) + 13)
        if snew > 'z': return chr(ord(snew) - 26)
        elif snew >= 'm': return snew
        elif snew > 'Z': return chr(ord(snew) - 26)
        return snew
    return "".join(r13(s) if s.isalpha() else s for s in m)

def rot13 (m):
    def r13(s):
        return chr(ord(s) + 13) if s.upper() < 'N' else chr(ord(s) - 13)
    return "".join(r13(s) if s.isalpha() else s for s in m)


def rot13_2(m):
    def r13(s):
        if s > 'm': return chr(ord(s) - 13)
        elif s >= 'a': return chr(ord(s) + 13)
        elif s > 'M': return chr(ord(s) - 13)
        else: return chr(ord(s) + 13)
    return "".join(r13(s) if s.isalpha() else s for s in m)


print(rot13('Test') == "Grfg")
print(rot13('test.assert_equals(rot13("test"),"grfg")'))
print(ord('Z') - ord('A'))
for i in range(ord('a'), ord('Z')+1):
    print(chr(i) + " = " + str(i))

"""
test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")
"""