"""For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel."""
def disemvowel_v1(string):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for i in vowels:
        string = string.replace(i, "")
    return string

def disemvowel(string):
    # vowelsDict = {'a':'', 'A':'', 'e':'', 'E':'', 'i':'', 'I':'', 'o':'', 'O':'', 'u':'', 'U':''}
    # vowelsDict = {i:'' for i in 'aAeEiIoOuU'}
    # transTable = str.maketrans({i:'' for i in 'aAeEiIoOuU'})
    return string.translate(str.maketrans({i:'' for i in 'aAeEiIoOuU'}))

#   !!! working BEST
#    return string.translate(str.maketrans('','','aeiouAEIOU'))

#   !!! Don't work in my system
#    return string.translate(None, "aeiouAEIOU")

#    return "".join(c for c in string if c.lower() not in "aeiou")

print(disemvowel("This website is for losers LOL!"))
help(str.maketrans)

"""                              "Ths wbst s fr lsrs LL!")
"""