"""
@TODO implementujte dle zadání cvičení 8
"""


class Card:
    """
    Třída pro reprezentaci hracích karet
    """
    ranks = {
        2: ['dvojka', 'ová'],
        3: ['trojka', 'ová'],
        4: ['čtyřka', 'ová'],
        5: ['pětka', 'ová'],
        6: ['šestka', 'ová'],
        7: ['sedmička', 'ová'],
        8: ['osmička', 'ová'],
        9: ['devítka', 'ová'],
        10: ['desítka', 'ová'],
        11: ['spodek', 'ový'],
        12: ['královna', 'ová'],
        13: ['král', 'ový'],
        14: ['eso', 'ové'],
    }

    suits = {
        's': 'srdc',
        'k': 'kár',
        'p': 'pik',
        't': 'tref',
    }

    def __init__(self, given_rank, given_suit):
        self._rank = None
        self._suit = None
        self.rank = given_rank
        self.suit = given_suit

    @property
    def rank(self):
        '''getter pomoci dekoratoru'''
        return self._rank

    @property
    def suit(self):
        """getter pomoci dekoratoru"""
        return self._suit

    @rank.setter
    def rank(self, given_rank):
        """setter pomoci dekoratoru"""
        if given_rank not in range(2, 15):      #self.ranks:
            raise TypeError("Zadaná hodnota pro kartu je neplatná!")
        self._rank = given_rank

    @suit.setter
    def suit(self, given_suit):
        """setter pomoci dekoratoru"""
        if given_suit not in self.suits:
            raise TypeError("Zadaná barva pro kartu je neplatná!")
        self._suit = given_suit

    def black_jack_rank(self):
        """
        Metoda vrací hodnotu karty dle pravidel pro Black Jack
        :return:
        """
        if self.rank > 10:
            if self.rank == 14:
                return 11
            return 10
        return self.rank

    def __eq__(self, other):
        """
        eq - equal tedy rovnost
        self == other
        """
        return self.black_jack_rank() == other.black_jack_rank()

    def __lt__(self, other):
        """
        lt - less then
        self < other
        """
        return self.black_jack_rank() < other.black_jack_rank()

    def __le__(self, other):
        """
        le -less than or equal to
        self <= other
        """
        return self.black_jack_rank() <= other.black_jack_rank()

    def __gt__(self, other):
        """
        gt - greater then
        self > other
        """
        return self.black_jack_rank() > other.black_jack_rank()

    def __ge__(self, other):
        """
        ge - greater than or equal to
        self >= other
        """
        return self.black_jack_rank() >= other.black_jack_rank()

    def __str__(self):
        """ Vrátí vhodnou textovou reprezentaci našeho vlastního typu - Card """
        str_card = '{0}{1} {2}'.format(self.suits.get(self._suit),
                                       self.ranks.get(self._rank)[1],
                                       self.ranks.get(self._rank)[0])
        return str_card


if __name__ == '__main__':
    pass
