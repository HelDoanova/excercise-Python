# -*- coding: utf-8 -*-

"""
Úkol 6.
Vaším dnešním úkolem je vytvořit program, který o zadaném textu zjistí některé
údaje a vypíše je na standardní výstup. Hlavním smyslem cvičení je procvičit
si práci s regulárními výrazy, takže pro plný bodový zisk je nutné použít k
řešení právě tento nástroj.

Program musí pracovat s obecným textem, který bude zadaný v souboru. Jméno
souboru bude zadáno jako vstupní parametr funkce main, která by měla být
vstupním bodem programu. Samozřejmě, že funkce main by neměla řešit problém
kompletně a měli byste si vytvořit další pomocné funkce. Můžete předpokládat,
že soubor bude mít vždy kódování utf-8 a že bude psaný anglicky, tedy jen
pomocí ASCII písmen, bez české (či jiné) diakritiky.

Konkrétně musí program zjistit a vypsat:

1. Počet slov, která obsahují právě dvě samohlásky (aeiou) za sebou. Například
slovo bear.

2. Počet slov, která obsahují alespoň tři samohlásky - například slovo atomic.

3. Počet slov, která mají šest a více znaků - například slovo terrible.

4. Počet řádků, které obsahují nějaké slovo dvakrát.

Podrobnější zadání včetně příkladu je jako obvykle na elearning.tul.cz
"""
import re

def main(file_name):
    """ Zpracuje soubor a volá další funkce"""
    with open(file_name, "r", encoding="utf8") as text_file:
        words = text_file.read()
    text_file.close()
    with open(file_name, "r", encoding="utf8") as text_file:
        lines = [line.rstrip('\n') for line in text_file]
    text_file.close()

    words = words.lower()
    words = words.split()
    words = remove_duplicate_words(words)

    print(two_vowel(words))
    print(three_vowel(words))
    print(six_character(words))
    print(duplicate_words_line(lines))


# Počet slov, která obsahují nejméně dvě samohlásky (aeiyou) za sebou.
# Například slovo bear.
# Stačí nám najít jen 2 samohlásky za sebou
# Pokud jich je více zákonitě tam musí být 2 za sebou
def two_vowel(words):
    """ Najde slova, která obsahují nejméně dvě samohlásky (aeiyou) za sebou. """
    counter = 0
    for word in words:
        temp = re.findall('[aeiyou]{2}', word)  # najde 2 samohlásky jdoucí po sobě ['io']
        if len(temp) >= 1:  # zkontroluje zda temp není prázdný
            counter += 1
    return counter


# Počet slov, která obsahují alespoň tři samohlásky - například slovo atomic.
def three_vowel(words):
    """ Najde slova, která obsahují alespoň tři samohlásky. """
    counter = 0
    for word in words:
        temp = re.findall('[aeiyou]', word)  # ['o', 'i', 'o', 'u']
        if len(temp) >= 3:  # zkontroluje jestli slovo obsahuje 3 samohlásky
            counter += 1
    return counter


# Počet slov, která mají šest a více znaků - například slovo terrible.
def six_character(words):
    """ Najde slova, která mají šest a více znaků. """
    counter = 0

    for word in words:
        temp = re.findall('[a-z]', word)  # ['o', 'b', 'v', 'i', 'o', 'u', 's']
        if len(temp) > 5:  # kontrola zda temp obsahuje alespon 6 znaků
            counter += 1
    return counter


# Počet řádků, které obsahují nějaké slovo dvakrát.
def duplicate_words_line(lines):
    """ Najde řádky, které obsahují nějaké slovo dvakrát. """
    counter = 0  # počítadlo řádků, které obsahují nějaké slovo dvakrát
    for line in lines:
        new_words = []
        count = 0  # počítadlo stejných slov v řádku
        words = line.split()
        for word in words:
            word = word.lower()
            temp = re.findall('[a-z\']*', word)  # ['obvious', '']

            # ošetření slova začínajícího v uvozovkách "glance -> ['', 'glance', '']
            # na prvním místě jsou uvozovky - galnce tedy musíme přesunout na první pouzici
            if len(temp[0]) == 0:
                temp[0] = temp[1]
            temp = temp[0]
            if temp not in new_words:
                new_words.append(temp)
            else:
                count += 1
        if count > 0:
            counter += 1

    return counter


# ošetření 2.zpusob
# temp2 = re.findall('^"[a-z\']*', word)  # ['obvious', '']  # if temp2 == 0:
def remove_duplicate_words(words):
    """ Odstraní duplicitní slova z textového souboru. """
    new_words = []
    for word in words:
        temp = re.findall('[a-z\']*', word)  # ['obvious', '']

        # ošetření slova začínajícího v uvozovkách "glance -> ['', 'glance', '']
        # na prvním místě jsou uvozovky - galnce tedy musíme přesunout na první pouzici
        if len(temp[0]) == 0:
            temp[0] = temp[1]
        temp = temp[0]
        if temp not in new_words:
            new_words.append(temp)
    return new_words


# 'cv06_test.txt'
# 'simple.txt'
if __name__ == '__main__':
    main('simple.txt')
