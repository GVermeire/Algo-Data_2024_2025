# aangezien elk karakter die geen letter is een scheidingsteken is vragen ze eerst te splitsen
def woorden_splitsen(bestand_locatie):
    try:
        # open het bestand en lees de inhoud in
        with open(bestand_locatie, "r") as bestand: # r = read = lezen, en we open het als bestand, mag eender welke naam zijn
            tekst = bestand.read()

        woorden = tekst.split()

