def mergesort(lijst: list):
    # Basisgeval: Als de lijst één element of leeg is, is deze al gesorteerd
    if len(lijst) <= 1:
        return lijst

    # Vind de helft om de lijst op te splitsen
    lengte = len(lijst)
    midden = lengte // 2

    # Verdeel de lijst in tweeën
    lijst1 = mergesort(lijst[:midden])
    lijst2 = mergesort(lijst[midden:])

    # Combineer de gesorteerde helften
    return merge(lijst1, lijst2)


def merge(left: list, right: list):
    sorted_list = []
    i = j = 0

    # Sorteer en voeg elementen van beide lijsten samen
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Voeg resterende elementen toe
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list