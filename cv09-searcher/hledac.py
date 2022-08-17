"""
Implementujte program dle zadání úlohy 9. na elearning.tul.cz

Vytvořte program, který prohledá zadaný textový
soubor a nejde v něm řádky, na kterých se vyskytuje hledaný vzor. Případně více
vzorů. Tyto řádky pak vypíše na obrazovku a přidat k ním jejich čísla v původním
souboru.

Tak trochu se toto chování podobá unixovému příkazu grep, přesněji
řečeno grep -n.  Ten můžete případně použít pro kontrolu. Nicméně váš program
toho bude umět v mnoha ohledech méně a v jednom více (vyhledávání více vzorů
najednou). Nejde tedy o to vytvářet 100% kopii příkazu grep.

Program musí jít  ovládat z příkazové řádky. Základním parametrem zadávaným
vždy, je jméno souboru. Pokud jméno souboru není zadané program nemůže pracovat
a měl by v takovém případě zobrazit nápovědu.

Druhý parametr  parametr -s --search bude volitelný. Může být následován
libovolným počtem n slov. Samozřejmě, pokud je tam parametr -s musí tam být to
slovo alespoň jedno (tedy n >= 1).  Pokud není zadané hledané slovo, musí
program opět vypsat chybu nebo nápovědu.
 """
import argparse


def load_file(input_file):
    '''
    načte uživatelem zadaný soubor
    '''
    with open(input_file, 'r') as file:
        data = file.read()
    return data


def main_solver(input_file, input_search_word):
    '''
    hlavni aplikacni logika - vyresi zadanou ulohu
    '''
    my_file = load_file(input_file)
    lines = my_file.split('\n')
    original_indexes = []
    txt_lines = []
    tmp = []

    for index, line in enumerate(lines):
        # pokud nezadáme parametr -s = vypíší se všechny řádky
        if input_search_word is None:
            txt_lines.append(line)
            original_indexes.append(index)
        else:
            for word in input_search_word:
                if word in line:
                    tmp.append(word)
            if len(tmp) == len(input_search_word):
                txt_lines.append(line)
                original_indexes.append(index + 1)
        tmp = []
    return original_indexes, txt_lines


def parse_args():
    '''
    zpracuje argumenty prikazove radky
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="input file name")
    parser.add_argument("-s", "--search", nargs='+', help="input search word/words")
    args = parser.parse_args()

    if args.filename is None:
        parser.error("nemuzu pracovat bez vstupniho souboru")

    original_indexes, txt_lines = main_solver(args.filename, args.search)
    print_on_terminal(original_indexes, txt_lines)


def print_on_terminal(original_indexes, txt_lines):
    ''' vypise vysledky do terminálu '''
    for index, line in enumerate(txt_lines):
        tmp = str(original_indexes[index]) + ":" + line
        print(tmp)


if __name__ == '__main__':
    parse_args()
