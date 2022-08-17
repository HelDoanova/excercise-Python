"""
Vytvorte funkce encrypt a decrypt pro Caesarovu sifru.
Kompletni zadani v elearningu.
"""

def encrypt(word, offset):
    """
    :param word - slovo k zasifrovani
    :param offset - znakovy posun
    :return: zasifrovane slovo
    """
    word = list(word)
    encrypted = ""
    for i in word:
        char = ord(i)
        if 91 > char > 64:
            encrypted += chr((char + offset - 65) % 26 + 65)
        elif 123 > char > 96:
            encrypted += chr((char + offset - 97) % 26 + 97)
        else:
            encrypted += i

    return encrypted


def decrypt(word, offset):
    """
    :param word - zasifrovane slovo
    :param offset - znakovy posun
    :return: desifrovane slovo
    """
    return encrypt(word, -offset)

'''
if __name__ == "__main__":
    original = 'VeLkA MaLa+'
    vzor = 'OxEdT FtEt'
    vysledek = encrypt(original, 19)
    print(vysledek)

    vzor2 = 'VeLkA MaLa'
    original2 = 'OxEdT FtEt+'
    vysledek2 = decrypt(original2, 19)
    print(vysledek2)
'''