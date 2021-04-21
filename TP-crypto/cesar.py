#Caesar cipher
def letterCaesar(l, nb):
    """
    letterCaesar: function that applies Caesar's cipher
    on only one letter.
    """
    if l == " ":
        return l

    asc = ord(l)
    asc += nb
    if l <= 'Z' and l >= 'A':
        if asc > ord('Z'):
            asc = ord('A') + asc - ord('Z')-1
        if asc < ord('A'):
            asc = ord('Z') - (ord('A') - asc)+1
        return chr(asc)

    if l <= 'z' and l >= 'a':
        if asc > ord('z'):
            asc = ord('a') + asc - ord('z') -1
        if asc < ord('a'):
            asc = ord('z') - (ord('a') - asc) +1
        return chr(asc)
    
    raise ValueError("Error: value is not a letter")

def letterCaesarMod(l, nb):
    if l == " ":
        return l
    asc = ord(l)
    asc += nb

    if l <= 'Z' and l >= 'A':
        if asc > ord('Z'):
            asc = ord('A') + asc % ord('Z')-1
        if asc < ord('A'):
            asc = ord('Z') - (ord('A') - asc) +1
        return chr(asc)

    if l <= 'z' and l >= 'a':
        if asc > ord('z'):
            asc = ord('a') + asc % ord('z')-1
        if asc < ord('a'):
            asc = ord('z') - (ord('a') - asc) +1
        return chr(asc)
    
    raise ValueError("Error: value is not a letter")


def wordCaesar(w, nb):
    """
    wordCaesar: function that applies Caesar's cipher
    on a whole word.

    Uses letterCaesar cipher.
    """
    l = len(w)
    res = ""

    for i in range(l):
        res += letterCaesar(w[i], nb)
    return res

def wordCaesarMod(w, nb):
    """
    wordCaesar: function that applies Caesar's cipher
    on a whole word.

    Uses letterCaesar cipher.
    """
    l = len(w)
    res = ""

    for i in range(l):
        res += letterCaesarMod(w[i], nb)
    return res

#tests
print(letterCaesar('a', 10))
print(wordCaesar("test", 1))
print(wordCaesar("Girls can code", 3))
print()
res = wordCaesar("Hello World", 10)
print(res)
res2 = wordCaesar(res, -10)
print(res2)
print()
print(wordCaesarMod("Girls can code", 3))
print()
res =wordCaesarMod("Hello World", 10)
print(res)
res2 = wordCaesarMod(res, -10)
print(res2)

