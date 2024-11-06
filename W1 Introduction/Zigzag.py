def samenvoegen(reeks1, reeks2):
    samengevoegd = []  # Lege lijst om de samengevoegde elementen op te slaan
    lengte = min(len(reeks1), len(reeks2))  # Zoek de lengte van de kortste reeks

    # Beurtelings de elementen van beide reeksen toevoegen
    for i in range(lengte):
        samengevoegd.append(reeks1[i])
        samengevoegd.append(reeks2[i])

    return samengevoegd


def weven(reeks1, reeks2):
    samengevoegd = []
    lengte_langste = max(len(reeks1), len(reeks2))  # Lengte van de langste reeks

    # Beurtelings toevoegen en bij kortste reeks herstarten wanneer deze eindigt
    for i in range(lengte_langste):
        samengevoegd.append(reeks1[i % len(reeks1)])  # Herstart de korte reeks indien nodig
        samengevoegd.append(reeks2[i % len(reeks2)])  # Herstart de korte reeks indien nodig
#De index die wordt gebruikt is i % len(reeks1), wat betekent dat als i groter is dan de lengte van reeks1, de index weer begint bij 0.
#De operator % (modulus) geeft de rest van de deling van i door de lengte van reeks1 terug
    return samengevoegd


def ritsen(reeks1, reeks2):
    samengevoegd = []
    lengte_kortste = min(len(reeks1), len(reeks2))  # Lengte van de kortste reeks

    # Eerst paarsgewijs elementen van beide reeksen toevoegen
    for i in range(lengte_kortste):
        samengevoegd.append(reeks1[i])
        samengevoegd.append(reeks2[i])

    # Voeg de resterende elementen van de langste reeks toe
    if len(reeks1) > lengte_kortste:
        samengevoegd.extend(reeks1[lengte_kortste:])
    elif len(reeks2) > lengte_kortste:
        samengevoegd.extend(reeks2[lengte_kortste:])

    return samengevoegd
