# efficiënte zoekalgoritme dat wordt gebruikt om een specifiek element te vinden in een gesorteerde lijst. Het werkt door de lijst steeds in tweeën te delen, waarbij het zoekgebied snel kleiner wordt, totdat het gewenste element is gevonden of de lijst is uitgeput.
def zoek(gesorteerd, x):
    links = 0
    rechts = len(gesorteerd) - 1

    #stopconditie, zoals in de les gezien vanaf indexen kruisen wil je stoppen met zoeken
    while links <= rechts:
        midden = (links + rechts) // 2

        if gesorteerd[midden] == x:
            return midden

        elif gesorteerd[midden] > x:
            rechts = midden - 1

        else:
            links = midden + 1

    return None
