"""
Úkol 5.
Napište program, který načte soubor large.txt a pro každé dveře vyhodnotí,
zda je možné je otevřít nebo ne. Tedy vyhodnotí, zda lze danou množinu uspořádat
požadovaným způsobem. Výstup z programu uložte do souboru vysledky.txt ve
formátu 1 výsledek =  1 řádek. Na řádek napište vždy počet slov v množině a True
nebo False, podle toho, zda řešení existuje nebo neexistuje.

Podrobnější zadání včetně příkladu je jako obvykle na elearning.tul.cz
"""
def load_file():
    '''Načte soubor a rovnou vytvoří další soubor, kam se budou ukládat výsedky'''
    with open("large.txt", "r", encoding="utf8") as text_file:
        lines = [line.rstrip('\n') for line in text_file]

    result_file = open("vysledky.txt", "w")
    n_doors = int(lines[0])
    index_line = 0

    for _ in range(n_doors):     # _ == door(jedny konkretni dvere) - kvuli pylint syntaxi
        opened = False
        index_line += 1
        alphabet_first = [0]*27     # pro začáteční písmena
        alphabet_last = [0]*27      # pro koncová písmena
        alphabet_double = [0]*27    # pro slova, která začínají a končí na stejné písmeno

        n_words = int(lines[index_line])
        for i in range(index_line + 1, index_line + n_words + 1):
            first_letter = lines[i][0]          # j = index_line? | [0] - prvni pismeno
            last_letter = lines[i][-1]          # j = index_line? | [-1] - posledni pismeno
            alphabet_first[ord(first_letter) - 97] += 1   # přičte 1 k pozici daného písmene
            alphabet_last[ord(last_letter) - 97] += 1  # přičte 1 k pozici daného písmene
            if first_letter == last_letter:
                alphabet_double[ord(first_letter) - 97] += 1  # přičte 1 k pozici daného písmene

        # výsledkem je pole, které nám znázorní kolikrát je v sekvenci slov písmeno,
        # na které nic již nenavazuje
        index_line = n_words + index_line       #posun na dalsi dvere
        opened = opening_doors(alphabet_first, alphabet_last, alphabet_double)
        result_file.write("%d %r\n" % (n_words, opened))

    text_file.close()
    result_file.close()


def opening_doors(alphabet_first, alphabet_last, alphabet_double):
    '''Zde ověřujeme zda daná sekvence slov na sebe navazuje či nikoli'''
    positive = 0    # pocet 1
    negative = 0    # pocet -1
    different = 0   # kdyz se vyskytuje jine cislo pr.2
    for letter_f, letter_l, doubs in zip(alphabet_first, alphabet_last, alphabet_double):
        # kontrola slov, která začínají a končí na stejné písmeno,
        # pokud zde je a nenavazuje vypíše se False
        if doubs != 0 and (letter_f == letter_l == doubs):
            return False

        letter = letter_f - letter_l
        if letter != 0:
            if letter == 1:
                positive += 1
            elif letter == -1:
                negative += 1
            else:
                different += 1
    # může nastat pouze situace, kdy daná sekvence slov začne a končí jiným písmenem
    # (začne: 1 | končí:-1)
    # nebo když začíná a končí stejným písmenem (začne: 0 | končí: 0)
    # v ostatních případech sekvence slov na sebe nenavazuje
    if positive <= 1 and negative <= 1 and different == 0:
        return True
    return False


if __name__ == '__main__':
    load_file()
