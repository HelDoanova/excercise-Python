# -*- coding: utf-8 -*-

"""
@TODO - vyřešit úkol 12.

Podrobné zadání jako obvykle na https://elearning.tul.cz

"""
import time
from itertools import permutations


def erotosthenes_sieve(min_number, max_number):
    """
    Eratosthenovo síto -  algoritmus pro nalezení všech prvočísel menších
    než zadaná horní mez
    """
    mem = max_number + 1
    #numbers = [True for i in range(mem)]
    numbers = [True] * mem #EDIT: faster
    numbers[0] = False
    numbers[1] = False
    for i in range(2, int(max_number ** 0.5 + 1)):
        if numbers[i]:
            for j in range(i*i, mem, i):
                numbers[j] = False
    primes_list = []
    for i in range(min_number, mem):
        if numbers[i]:
            primes_list.append(i)
    return primes_list


def take_repeated_3more_digits(primes_list):
    """
    Vyhledá čísla, která obsahují nějakou číslici 3x nebo vícekrát
    """
    primes_new = []
    for prime in primes_list:
        temp = str(prime)
        three_digit = False
        for j in range(0, len(temp)):
            counter = 0
            for k in range(0, len(temp)):
                if temp[j] == temp[k]:
                    counter += 1
                if counter >= 3:
                    three_digit = True
                    break
        if three_digit:
            primes_new.append(prime)
    return primes_new


def get_possible_pattern():
    """
    Najde všechny možnosti, jak by mohlo číslo vypadat
    x - statický snak
    o - znak, který se bude nahrazovat
    Na posledním místě čísla nemohou být všechna číslice,
    proto se počítá jen s 5 místama a následně se doplní šestí statické
    """
    patterns_list = []
    perm = set(permutations(["x", "x", "o", "o", "o"]))
    for i in perm:
        temp = list(i)
        temp.append("x")
        patterns_list.append(temp)
    return patterns_list


def get_pattern_position(patterns_list):
    """
    Najde všechny pozice v listu, na kterých je znak "o"
    Výsledkem jsou listy pozic z jednotlivých patternů
    """
    pattern_positions = []
    for i in patterns_list:
        temp = []
        for position, item in enumerate(i):
            if item == "o":
                temp.append(position)
        pattern_positions.append(temp)
    return pattern_positions


def create_patterns_of_number(number, pattern_position_list):
    """
    Zadané číslo převede na string, a poté na daných pozicích z aktuálního patternu
    postupně nahrazuje znaky číslicemi 0-9
    Výsledkem je nested list, který obsahuje 10 listů
    Každý list reprezentuje jeden pattern(celkem máme 10 patternů proto 10 listů)
    V každém listu se nachází 10 čísel
    (v 1 patternu lze postupně nahradit dané pozice číslicemi 0-9, proto 10 čísel)
    """
    number = str(number)
    patterns_of_number = []
    for pattern in pattern_position_list:
        p_1 = pattern[0]     # first position
        p_2 = pattern[1]     # second position
        p_3 = pattern[2]     # third position
        replace_iterator = 0
        temp = []
        while replace_iterator < 10:
            replace_digit = str(replace_iterator)
            replaced_number = number[:p_1] + replace_digit + number[p_1 + 1:]
            replaced_number = replaced_number[:p_2] + replace_digit + replaced_number[p_2 + 1:]
            replaced_number = replaced_number[:p_3] + replace_digit + replaced_number[p_3 + 1:]
            temp.append(int(replaced_number))
            replace_iterator += 1
        patterns_of_number.append(temp)
    return patterns_of_number


def check_patterns_prime_numbers(seq, primes_repeated_list):
    """
    Zkontroluje vytvořený list z metody - create_patterns_of_number(number)
    Pokud se číslo nachází v primes_repeated_list(a tudíž je prvočíslo),
    přidá se do nového listu, který bude obshaovat jen prvočísla
    """
    new_seq = []
    for i in seq:
        if i in primes_repeated_list:
            new_seq.append(i)
    return new_seq


def find_secret_sequence(primes_repeated_list, pattern_position_list):
    """
    Metoda pro nalezení správné sekvence čísel
    """
    seq_found = False
    sequence = []

    for num in primes_repeated_list:
        patterns_of_number = create_patterns_of_number(num, pattern_position_list)
        for seq in patterns_of_number:
            seq = check_patterns_prime_numbers(seq, primes_repeated_list)
            if len(seq) == 8:
                seq_found = True
                for number in seq:
                    sequence.append(number)
                break
        if seq_found:
            break
    return sequence


def make_file(secret_nums):
    """
    Metoda pro vytvoření souboru s tajnou sekvencí čísel
    """
    filename = "new_codes.txt"
    with open(filename, 'w') as file:
        for number in secret_nums:
            file.write("%s\n" % number)


if __name__ == '__main__':
    # spuštění časovače
    start = time.time()

    # vytvoření patternů a získání jejich pozic
    patterns = get_possible_pattern()
    pattern_position = get_pattern_position(patterns)

    # vyhledání prvočísel a následné získání tajné sekvence prvočísel
    primes = erotosthenes_sieve(100000, 999999)
    primes_repeated = take_repeated_3more_digits(primes)
    secret_numbers = find_secret_sequence(primes_repeated, pattern_position)

    make_file(secret_numbers)

    # ukončení časovače a výpis, jak dlouho program běžel
    end = time.time()
    time_of_running = end - start
    print("Doba trvání: " + str(time_of_running))
