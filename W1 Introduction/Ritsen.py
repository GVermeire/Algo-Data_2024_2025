# inefficiente optie voor samenvoegen, efficienter is om eerst lengte = min(len(..), ...) te doen
def samenvoegen(lst1: list, lst2: list):
    rits = []
    lengte1 = len(lst1)
    lengte2 = len(lst2)
    if lengte1 == lengte2:
        for i in range(lengte1):
            rits.append(lst1[i])
            rits.append(lst2[i])
        return rits
    elif lengte1 < lengte2:
        for i in range(lengte1):
            rits.append(lst1[i])
            rits.append(lst2[i])
        return rits
    else:
        for i in range(lengte2):
            rits.append(lst1[i])
            rits.append(lst2[i])
        return rits

def weven(reeks1, reeks2):
    samengevoegd = []
    lengte_langste = max(len(reeks1), len(reeks2))  # Lengte van de langste reeks

    # Beurtelings toevoegen en bij kortste reeks herstarten wanneer deze eindigt
    for i in range(lengte_langste):
        samengevoegd.append(reeks1[i % len(reeks1)])  # Herstart de korte reeks indien nodig
        samengevoegd.append(reeks2[i % len(reeks2)])  # Herstart de korte reeks indien nodig

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

