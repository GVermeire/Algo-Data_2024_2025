def sort(lijst):
    if len(lijst) <= 1:
        return  # Basiscasus: niets te doen bij een lege of een enkele item-lijst

    # Kies de spil (midden)
    midden = len(lijst) // 2
    spil = lijst[midden]

    # Partitioneer in lijsten kleiner en groter dan de spil
    lijstkleiner = [x for x in lijst if x < spil]
    lijstgelijk = [x for x in lijst if x == spil]
    lijstgroter = [x for x in lijst if x > spil]

    # Roep recursief sorteerfunctie aan
    sort(lijstkleiner)
    sort(lijstgroter)

    # Leeg de lijst en voeg de gesorteerde elementen toe
    lijst.clear()
    lijst.extend(lijstkleiner + lijstgelijk + lijstgroter)