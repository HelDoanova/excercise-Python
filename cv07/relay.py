"""
Cvičení 7. - práce s daty

Vaším dnešním úkolem je spojit dohromady data, uložená ve dvou různých
souborech. První soubor obsahuje výsledky závodu - jména a časy závodníků. Druhý
pak obsahuje databázi závodníků uloženou jako JSON - mimo jiné jejich id. Cílem
je vytvořit  program, který tyto data propojí, tedy ke každému závodníkovi ve
štafetě najde jeho id. Případně také nenajde, data nejsou ideální. I tuto
situaci ale musí program korektně ošetřit.  Výsledky programu bude potřeba
zapsat do dvou souborů.

Kompletní zadání je jako vždy na https://elearning.tul.cz/

"""
import json
import re
from bs4 import BeautifulSoup


def load_html(html_file):
    """ Načte soubor html """
    with open(html_file, 'r', encoding="utf8") as html:
        soup = BeautifulSoup(html, 'html.parser')
    results = []
    for paragraph in soup.find_all('p'):
        results.append(paragraph.text)
    html.close()
    return results


def load_json(json_file):
    """ Načte soubor json """
    with open(json_file, 'r', encoding="utf8") as json_f:
        competitors_l = json.load(json_f)
    json_f.close()
    return competitors_l


def get_discipline(index):
    """ Vrátí list konkrétní disciplíny - rozděleno i na muže a ženy """
    # * pro určení jednotlivých položek týmu
    temp = index.replace('), ', ';').replace(')', '*').replace('(', '*')
    temp = temp.split(';')
    discipline = []
    for line in temp:
        discipline.append(line.split('*'))  # * rozděluje jednotlivé položky týmu
    return discipline


def get_team(discipline):
    """ Vrátí list se jmény jednotlivých členů týmů """
    teams = []
    for team in discipline:
        temp = team[2].replace(', ', ',')   # odstraníme mezery za čárkou
        teams.append(temp.split(','))
    return teams


def get_time(discipline):
    """ Vrátí list s časy týmů """
    times = []
    for time in discipline:
        temp = re.sub(r'[^\d:]+', '', time[1])  # odstraníme všechno kromě číslic a dvojtečky
        times.append(temp)
    return times


def get_id(competitor, competitors):
    """
    Porovná jestli je jméno závodníka ze souboru result i v souboru competitors,
    či se shoduje nebo ne. A pokud ano vrátí jeho id.
    Pokud ne, id bude obsahovat hodnotu "False"
    """
    identificator = 'False'    # předdefinujeme id na False
    for compet in competitors:
        full_name = compet['firstname'] + ' ' + compet['lastname'] # spojí položky do jedné
        if competitor == full_name:
            identificator = compet['id']
    return identificator


def organizer(results, competitors):
    """
    Zde se pracuje s oběma soubory a pomocí pomocných funkcí se vytvoří
    result_list, který obsahuje id, výsledné pořadí, čas závodníka a pokud je id False tak i
    klíč "no-match", kde je uloženo závodníkovo jméno
    """
    index = results.index('Relay')
    women_index = results[index + 2]
    men_index = results[index + 4]
    women_discipline = get_discipline(women_index)
    men_discipline = get_discipline(men_index)
    women_teams = get_team(women_discipline)
    men_teams = get_team(men_discipline)
    women_times = get_time(women_discipline)
    men_times = get_time(men_discipline)
    result_list = list()
    for team in men_teams:
        for competitor in team:
            compet = {}
            compet['id'] = get_id(competitor, competitors)
            index = men_teams.index(team)
            compet['result'] = index + 1
            compet['time'] = men_times[index]
            if compet['id'] == 'False':
                compet['no_match'] = competitor
            result_list.append(compet)
    for team in women_teams:
        for competitor in team:
            compet = {}
            compet['id'] = get_id(competitor, competitors)
            index = women_teams.index(team)
            compet['result'] = index + 1
            compet['time'] = women_times[index]
            if compet['id'] == 'False':
                compet['no_match'] = competitor
            result_list.append(compet)
    return result_list


def output_json(result_list):
    """
    Uloží list slovníků do souboru output.json tak jak je požadováno
    v zadání.
    """
    with open('output.json', 'w') as output:
        output.write(json.dumps(result_list, indent=4, sort_keys=True))


def output_compare(result_list):
    """ Vytvoří textoví soubor kde je na každém řádku id a pořadí závodníka (vzestupně)"""
    compare = []
    with open('compare.txt', 'w') as output:
        for competitor in result_list:
            if competitor['id'] != 'False':
                identificator = competitor['id']
                result = competitor['result']
                line = [identificator, result]
                compare.append(line)
        # seřadím vzestupně podle id - tedy podle prvního prvku podlistu [id, pořadí]
        compare.sort(key=lambda x: x[0])
        count = 1
        for index in compare:
            if count == len(compare):
                output.write("%d %d" % (index[0], index[1]))
            else:
                output.write("%d %d\n" % (index[0], index[1]))
                count += 1
    output.close()


def output_errors(competitors, result_list):
    """
    Vytvoří textoví soubor kde je na každém řádku jméno závodníka,
    kterého program nemohl zařadit.
    Tento závodník má v souboru output.json hodnoti id False.
    """
    with open('errors.txt', 'w') as output:
        errors = []
        for first, second in zip(competitors, result_list):
            if second['id'] == 'False':
                full_name = first['firstname'] + ' ' + first['lastname']
                errors.append(full_name)
        count = 1
        for name in errors:
            if count == len(errors):
                output.write("%s" % name)
            else:
                output.write("%s\n" % name)
                count += 1
    output.close()


if __name__ == '__main__':
    results_data = load_html("result.html")
    competitors_data = load_json("competitors.json")
    result_list_organizer = organizer(results_data, competitors_data)
    output_json(result_list_organizer)
    output_compare(result_list_organizer)
    output_errors(competitors_data, result_list_organizer)
