import re
from collections import defaultdict


def woorden_splitsen(bestand):
    with open(bestand, 'r', encoding ='utf-8') as f:
        tekst = f.read()

    woorden = re.findall(r'[a-zA-Z]+', tekst)

    return woorden

def woorden_tellen(bestand):
    with open(bestand, 'r', encoding ='utf-8') as f:
        tekst = f.read().lower()

    woorden = re.findall(r'[a-zA-Z]+', tekst)

    woord_frequentie = defaultdict(int)

    for woord in woorden:
        woord_frequentie[woord] += 1

    return dict(woord_frequentie)