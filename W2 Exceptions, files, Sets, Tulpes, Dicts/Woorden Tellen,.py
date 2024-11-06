# aangezien elk karakter die geen letter is een scheidingsteken is vragen ze eerst te splitsen
from collections import defaultdict


def woorden_splitsen(bestand_locatie: str):
    try:
        # open het bestand en lees de inhoud in
        with open(bestand_locatie, "r") as file: # r = read = lezen, en we open het als bestand, mag eender welke naam zijn
            tekst = file.read()

        woorden = tekst.split()
        print(woorden)

    except FileNotFoundError:
        print("File not found")

# woorden_splitsen("data.txt")

def woorden_tellen(bestand_locatie: str) -> dict:
    woorden = woorden_splitsen(bestand_locatie)
    telling = defaultdict(int)
    for woord in woorden:
        woord = woord.lower()
        telling[woord] += 1

    return dict(telling)




