def dubbel(lst):
    # We maken een dictionary aan om de frequentie van elk element bij te houden
    frequenties = {}

    # Doorloop de lijst en vul de frequenties
    for nummer in lst:
        if nummer in frequenties:
            frequenties[nummer] += 1
        else:
            frequenties[nummer] = 1

    # Zoek naar het element dat precies 2 keer voorkomt
    for nummer, frequentie in frequenties.items():
        if frequentie == 2:
            return nummer

    # Als er geen element is dat twee keer voorkomt, return None
    return None

def dubbels(lijst):

    frequenties = {}

    for nummer in lijst:
        if nummer in frequenties:
            frequenties[nummer] += 1
        else:
            frequenties[nummer] = 1

    een_keer = set()
    meermaals = set()

    for nummer, frequentie in frequenties.items():
        if frequentie == 1:
            een_keer.add(nummer)
        else:
            meermaals.add(nummer)

    return een_keer, meermaals