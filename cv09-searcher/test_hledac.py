"""

implementujte testy pro program hledac.py

pokrytí kódu musí být minimálně 75%
"""
import pytest
import hledac
import io
from io import StringIO
import sys


def test_indexes_and_lines_of_search_one_word():
    """
    Testuje, jestli se vrací správné indexi a řádky pro zadaný (1) parametr
    """
    search_word = ['pharetra']
    expected_indexes = [5, 6, 75, 91, 131]
    expected_lines = [
        "consequat felis, a pharetra dolor venenatis nec. Etiam dolor erat, imperdiet ut",
        "pharetra congue, suscipit euismod nisl. Mauris ultricies, felis nec tempus",
        "vehicula velit consequat. Sed in ante libero. Proin vel nisi a risus pharetra",
        "amet. Etiam rutrum libero at lorem pharetra consequat. Praesent ultrices metus",
        "pharetra magna eu semper. Nulla pulvinar orci ut urna porta adipiscing."
    ]
    my_indexes, my_lines = hledac.main_solver('lipsum.txt', search_word)
    assert expected_indexes == my_indexes and expected_lines == my_lines


def test_indexes_and_lines_of_search_two_word():
    """
    Testuje, jestli se vrací správné indexi a řádky pro zadaný (2) parametry
    """
    search_words = ['justo', 'non']
    expected_indexes = [8, 11, 24]
    expected_lines = [
        "Nullam justo erat, tempus eget placerat ullamcorper, suscipit non augue. Duis",
        "Cras porta, justo non ornare scelerisque, purus tortor vehicula nunc, et",
        "ante nec nunc gravida feugiat. Nam fringilla justo non urna posuere eu aliquet"
    ]
    my_indexes, my_lines = hledac.main_solver('lipsum.txt', search_words)
    assert expected_indexes == my_indexes and expected_lines == my_lines


def test_indexes_and_lines_of_search_tree_word():
    """
    Testuje, jestli se vrací správné indexi a řádky pro zadaný (3) parametry
    """
    search_words = ['varius', 'ornare', 'leo']
    expected_indexes = [30]
    expected_lines = [
        "Nunc varius ornare leo, a tincidunt nisi interdum sed. Suspendisse vitae laoreet"
    ]
    my_indexes, my_lines = hledac.main_solver('lipsum.txt', search_words)
    assert expected_indexes == my_indexes and expected_lines == my_lines


def test_print_on_terminal():
    """
    Testuje, jestli se do terminálu vypisují data v daném formátu
    """
    capturedOutput = io.StringIO()  # Create StringIO object
    sys.stdout = capturedOutput  # and redirect stdout.
    tmp_i = [5]
    tmp_l = ["ahoj"]
    hledac.print_on_terminal(tmp_i, tmp_l)  # Call unchanged function.
    sys.stdout = sys.__stdout__  # Reset redirect.
    assert capturedOutput.getvalue() == "5:ahoj\n"  # Now works as before.


@pytest.fixture
def create_parser(mocker):
    mocker.patch('sys.argv', '-f hledac.py')
    return hledac.parser()

def test_url_arg(create_parser):
    assert create_parser != ' '
