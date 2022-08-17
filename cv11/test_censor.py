# -*- coding: utf-8 -*-

"""
@TODO: zde napiste svoje unit testy pro modul censor.py
"""
import io
import sys
import pytest
import censor


def test_quick_control():
    """
    Testuje, zda se správně odstraní případné nadbytečné mezery a značky \n
    """
    data ="Dneska\n\nje  ale krásné počasí"
    expected_output = ["Dneska", "\n", "je", " ", "ale", " ", "krásné", " ", "počasí"]
    output = censor.quick_control(data)
    assert expected_output == output

def test_quick_control_with_tag():
    """
    Testuje, zda se správně odstraní případné nadbytečné mezery a značky \n
    na datech, která obsahují i html tagy
    """
    data ="<html>\n\n\n\n\n<body>\n<h1>Ahoj   nazdar cau</h1>\n<p>"
    expected_output = ["", "<", "html", ">\n<", "body", ">\n<", "h1", ">", "Ahoj", " ", "nazdar", " ", "cau", "</", "h1", ">\n<", "p", ">", ""]
    output = censor.quick_control(data)
    assert expected_output == output

def test_clean_html_tag():
    """
    Testuje, zda se správně odstraní html tagy
    """
    data = "<html>\n<body>\n<h1>Ahoj nazdar cau</h1>\n<p>"
    expected_output = "\n\nAhoj nazdar cau\n"
    output = censor.clean_html_tag(data)
    assert expected_output == output

def test_forbidden_word_creator():
    """
    Testuje, zda se správně vytvoří list zakázaných slov
    """
    data = "kokos\npláž\ngepard\npomeranč\n"
    expected_output = ["kokos", "pláž", "gepard", "pomeranč"]
    output = censor.forbidden_word_creator(data)
    assert expected_output == output

def test_replace_forbidden_words():
    """
    Testuje, zda se správně nahradí zakázaná slova značkami #
    """
    input_html = ["Dneska", "\n", "je", " ", "ale", " ", "krásné", " ", "počasí"]
    input_forbidden_words = ["počasí", "je"]
    expected_output = ["Dneska", "\n", "##", " ", "ale", " ", "krásné", " ", "######"]
    output = censor.replace_forbidden_words(input_html, input_forbidden_words)
    assert expected_output == output

def test_program_output():
    """
    Testuje, zda se výsledek správně vypíše na terminál
    """
    censured_text = "Ahoj ##### cau"
    captured_output = io.StringIO()  # Create StringIO object
    sys.stdout = captured_output  # and redirect stdout.
    censor.program_output(censured_text, None)  # Call unchanged function.
    sys.stdout = sys.__stdout__  # Reset redirect.
    assert captured_output.getvalue() == "Ahoj ##### cau"  # Now works as before.

def test_censor_app():
    """
    Testuje, funkčnost hlavní metody
    """
    input_html = "muj_html.html"
    input_txt = "muj_list.txt"
    input_clean = False
    expected_output =["", "<", "html", ">\n<", "body", ">\n<", "h1", ">", "Ahoj", " ", "######", " ", "cau", "</", "h1", ">\n<", "p", ">", ""]
    output = censor.censor_app(input_html, input_txt, input_clean)
    assert expected_output == output
