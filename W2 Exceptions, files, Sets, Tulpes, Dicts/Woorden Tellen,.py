def woorden_splitsen(bestandslocatie: str) -> list:
    with open(bestandslocatie, 'r') as bestand:
        tekst = bestand.read()
        woorden = tekst.split()
    return woorden

woorden_splitsen("data.txt")

"""
def woorden_tellen(bestand_locatie: str) -> dict:
    woorden = woorden_splitsen(bestand_locatie)
    telling = defaultdict(int)
    for woord in woorden:
        woord = woord.lower()
        telling[woord] += 1

    return dict(telling)

woorden_tellen("data.txt")
"""




