


def is_palindrom(text):
    nowy_tekst = ""
    for char in text:
        if char.isalnum():
            nowy_tekst = nowy_tekst + char.lower()
    
    i=0
    j=len(nowy_tekst)-1
    while i < j:
        if nowy_tekst[i] != nowy_tekst[j]:
            return False
        i += 1
        j -= 1
    return True

text1 = "Eine güldne, gute Tugend: Lüge nie!"
text2 = "Kobyła ma mały bok."
text3 = "Míč omočím."
text4 = "abc"
if __name__ == '__main__':
    print(is_palindrom(text1))
    print(is_palindrom(text2))
    print(is_palindrom(text3))
    print(is_palindrom(text4))