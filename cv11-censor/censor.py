# -*- coding: utf-8 -*-

"""
@TODO - vyřešit úkol 11. - filtrování textu

Podrobné zadání jako obvykle na https://elearning.tul.cz

"""
import argparse
import re


def load_file(input_file):
    """
    načte soubor
    """
    with open(input_file, 'r') as file:
        data = file.read()
    return data


def clean_html_tag(html):
    """
    odstraní všechny html tagy
    """
    tag = re.compile('<.*?>')
    text = re.sub(tag, '', html)
    return text

def forbidden_word_creator(txt):
    """
    vytvoří list se zakázaným slovy
    """
    list_text = txt.replace('\n', ' ').strip()
    text = re.split(' ', list_text)
    return text


def quick_control(html):
    """
    rychlá kontrola textu(odstraní nadbytečné mezery a značky \n)
    """
    html_text = re.sub(r'\n+', '\n', html).strip()
    html_text = re.sub(' +', ' ', html_text)
    text = re.split(r'(\W+)', html_text)
    return text


def parse_args():
    """
    zpracuje argumenty příkazové řádky
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help=" input file for edit")
    parser.add_argument("-l", "--list", help="input file with forbidden words")
    parser.add_argument("-c", "--clean", action='store_true', help="remove html tags")
    parser.add_argument("-o", "--output", help="create output file, otherwise print on terminal")
    args = parser.parse_args()

    if args.input is None:
        parser.error("nemuzu pracovat bez vstupniho souboru")

    if args.list is None:
        parser.error("nemuzu pracovat bez seznamu zakázaných slov")

    censured_text = censor_app(args.input, args.list, args.clean)
    program_output(censured_text, args.output)


def program_output(censured_text, output):
    """
    pokud je zadán parametr -o vytvoří nová soubor a do něj zapíše výsledek,
    jinak se výsledek vypíše do terminálu
    """
    if output is None:
        for word in censured_text:
            print(word, end="")     # musi byt end, jinak se nezobrazuje správně
    else:
        with open(output, 'w') as file:
            for word in censured_text:
                file.write("%s" % (word))
            file.write("\n")


def replace_forbidden_words(html, forbidden_words):
    """
    nahradí zakázaní slova sekvencí #,
    sekvence je tak dlouhá jako slovo samotné
    """
    censored_text = []
    for word in html:
        if word in forbidden_words:
            replace = ''
            for _ in word:
                replace = replace + '#'
            censored_text.append(replace)
        else:
            censored_text.append(word)
    return censored_text


def censor_app(input_html, input_txt, input_clean):
    """
    hlavní metoda
    """
    if input_clean is False:
        html = quick_control(load_file(input_html))
    else:
        html = quick_control(clean_html_tag(load_file(input_html)))

    forbidden_words = forbidden_word_creator(load_file(input_txt))
    censored_text = replace_forbidden_words(html, forbidden_words)
    return censored_text


if __name__ == '__main__':
    parse_args()
