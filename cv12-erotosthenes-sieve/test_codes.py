# -*- coding: utf-8 -*-

"""
@TODO: zde napiste svoje unit testy pro program codes.py
"""
import pytest
import codes


def test_erotosthenes_sieve():
    """
    Testuje eratosthenovo síto, jestli najde všechna prvočísla od dolní do horní zadané meze
    """
    data_input_min = 0
    data_input_max = 70
    expected_output = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
    output = codes.erotosthenes_sieve(data_input_min, data_input_max)
    assert expected_output == output


def test_take_repeated_3more_digits():
    """
    Testuje zda vyhledá čísla, které obsahují nějakou číslici 3x nebo vícekrát
    """
    data_input = [100, 102, 111, 113, 222, 3033, 5555, 7321, 8322, 19999, 155895]
    expected_output = [111, 222, 3033, 5555, 19999, 155895]
    output = codes.take_repeated_3more_digits(data_input)
    assert expected_output == output


def test_get_possible_pattern():
    """
    Testuje, zda najde všechny možnosti, jak by mohlo číslo vypadat
    """
    expected_output = [['o', 'x', 'o', 'x', 'o', 'x'],
                       ['o', 'o', 'x', 'x', 'o', 'x'],
                       ['o', 'o', 'x', 'o', 'x', 'x'],
                       ['x', 'o', 'x', 'o', 'o', 'x'],
                       ['o', 'o', 'o', 'x', 'x', 'x'],
                       ['o', 'x', 'o', 'o', 'x', 'x'],
                       ['o', 'x', 'x', 'o', 'o', 'x'],
                       ['x', 'o', 'o', 'x', 'o', 'x'],
                       ['x', 'x', 'o', 'o', 'o', 'x'],
                       ['x', 'o', 'o', 'o', 'x', 'x']]

    output = codes.get_possible_pattern()
    all_pattern = False
    counter = 0
    for pattern_one in expected_output:
        for pattern_two in output:
            if pattern_one == pattern_two:
                counter += 1

    if counter == 10:
        all_pattern = True

    assert all_pattern


def test_get_pattern_position():
    """
    Tetuje, zda najde všechny pozice v listu, na kterých je znak "o"
    """
    data_input = [['o', 'x', 'o', 'x', 'o', 'x'],
                  ['o', 'o', 'x', 'x', 'o', 'x'],
                  ['o', 'o', 'x', 'o', 'x', 'x'],
                  ['x', 'o', 'x', 'o', 'o', 'x'],
                  ['o', 'o', 'o', 'x', 'x', 'x'],
                  ['o', 'x', 'o', 'o', 'x', 'x'],
                  ['o', 'x', 'x', 'o', 'o', 'x'],
                  ['x', 'o', 'o', 'x', 'o', 'x'],
                  ['x', 'x', 'o', 'o', 'o', 'x'],
                  ['x', 'o', 'o', 'o', 'x', 'x']]
    expected_output = [[0, 2, 4],
                       [0, 1, 4],
                       [0, 1, 3],
                       [1, 3, 4],
                       [0, 1, 2],
                       [0, 2, 3],
                       [0, 3, 4],
                       [1, 2, 4],
                       [2, 3, 4],
                       [1, 2, 3]]
    output = codes.get_pattern_position(data_input)
    assert expected_output == output


def test_create_patterns_of_number():
    """
    Testuje, zda metoda správně vytvoří list čísel,
    ve kterých na daných pozicích změní postupně znak na číslici 0-9
    """
    data_input_number = 112919
    data_input_pattern_position_list = [[2, 3, 4],
                                        [0, 2, 4],
                                        [0, 1, 3]]
    expected_output = [[110009, 111119, 112229, 113339, 114449, 115559, 116669, 117779, 118889, 119999],
                       [10909, 111919, 212929, 313939, 414949, 515959, 616969, 717979, 818989, 919999],
                       [2019, 112119, 222219, 332319, 442419, 552519, 662619, 772719, 882819, 992919]]

    output = codes.create_patterns_of_number(data_input_number, data_input_pattern_position_list)
    assert expected_output == output


def test_check_patterns_prime_numbers():
    """
    Testuje, zda metoda vrací list, který obsahuje pouze prvočísla
    """
    temp = codes.erotosthenes_sieve(100000, 999999)
    temp = codes.take_repeated_3more_digits(temp)
    data_input_primes_repeated = temp

    date_input_sequence = [100201, 111211, 122221, 133231, 144241, 155251, 166261, 177271, 188281, 199291]
    expected_output = [111211, 144241, 155251, 188281]

    output = codes.check_patterns_prime_numbers(date_input_sequence, data_input_primes_repeated)
    assert expected_output == output


def test_find_secret_sequence():
    """
    Testuje, zda metoda nalezne správnou sekvenci čísel
    """
    temp = codes.erotosthenes_sieve(100000, 999999)
    temp = codes.take_repeated_3more_digits(temp)
    data_input_primes_repeated = temp

    temp2 = codes.get_possible_pattern()
    temp2 = codes.get_pattern_position(temp2)
    data_input_pattern_position = temp2

    expected_output = [121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393]
    output = codes.find_secret_sequence(data_input_primes_repeated, data_input_pattern_position)
    assert expected_output == output
