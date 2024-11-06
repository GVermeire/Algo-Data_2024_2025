def bloedgroep_ouder(ouder, kind):

    ABO_ouder = ouder[:-1]
    ABO_kind = kind[:-1]

    rhesus_ouder = ouder[-1]
    rhesus_kind = kind[-1]

    mogelijke_bloedgroepen = set()

    if ABO_kind in["A", "B"]:
        if ABO_ouder in ["AB", ABO_kind]:
            mogelijke_bloedgroepen.update({"B", "AB", "O", "A"})
        elif ABO_ouder == "O" or ABO_ouder != ABO_kind:
            mogelijke_bloedgroepen.update({f"{ABO_kind}", "AB"})
    elif ABO_kind == "O":
        if ABO_ouder in ["O", "A", "B"]:
            mogelijke_bloedgroepen.update("B", "O", "A")
    elif ABO_kind == "AB":
        if ABO_ouder == "A":
            mogelijke_bloedgroepen.update({"B", "AB"})
        elif ABO_ouder == "B":
            mogelijke_bloedgroepen.update({"A", "AB"})
        elif ABO_ouder == "AB":
            mogelijke_bloedgroepen.update({"A", "B", "AB"})

    mogelijke_rhesus = set()

    if rhesus_kind == "+" and rhesus_ouder == "-":
        mogelijke_rhesus.add("+")
    else:
        mogelijke_rhesus.update("+", "-")

    resultaat = set()

    for bloedgroep in mogelijke_bloedgroepen:
        for rhesus in mogelijke_rhesus:
            resultaat.add(bloedgroep + rhesus)

    return resultaat