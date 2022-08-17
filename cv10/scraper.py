# -*- coding: utf-8 -*-

"""
@TODO - vyřešit úkol 10. - zpracování HTML
"""

import re
import sys
from bs4 import BeautifulSoup
import requests


def get_email(soup):
    """ Najde všechny emaily na stránce a provede i validaci """
    emails_text = set(re.findall(
        r"[a-zA-Z0-9+.!#$%&'*+/=?^_`{|}~-]+(?:@|#)[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+",
        str(soup)))
    validated = []
    for email in emails_text:
        correct_email = ""
        for char in email:
            if char == '@' or char == '.' or char.isdigit() or char.islower():
                correct_email += char
            elif char is str('#'):
                correct_email += '@'
        validated.append(correct_email)
    return validated


def get_link(soup):
    """ Najde na stránce všechny odkazy """
    links = []
    for link in soup.findAll('a'):
        href = link.get('href')
        if '.html' in href and 'http' not in href:
            links.append(href)
    return links


def get_soup(url):
    """ Vytvoří přehledný content stránky """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def web_scraper(base_url):
    """ Hlavní funkce """
    page = "index.html"
    all_link = {}
    emails = []
    url = base_url + page
    all_link[page] = get_link(get_soup(url))
    temp = all_link.copy()

    for _ in range(2):
        for link in all_link.copy():
            for page in temp[link]:
                if page not in temp.keys():
                    url = base_url + page
                    soup = get_soup(url)
                    new_links = get_link(soup)
                    temp[page] = new_links
            all_link = temp

    for key in all_link.keys():
        url = base_url + key
        emails.append(get_email(get_soup(url)))

    make_result_file(all_link, emails)


def make_result_file(all_link, emails):
    """ Vytvoří soubor s mapou stránek a s emaily """
    filename = "scrap_result.txt"
    with open(filename, 'w') as file:
        file.write(str(all_link) + '\n')
        file.write('\n')
        for i, _ in enumerate(all_link.keys()):
            for mail in emails[i]:
                file.write(mail + '\n')


if __name__ == '__main__':
    web_scraper(str(sys.argv[1]))
