def isISBN13(code):
    if not(
        isinstance(code, str) and
        len(code) == 13 and
        code.isdigit()
    ):
        return False

    if code[:3] not in ('978', '979'):
        return False

    controle = 0
    for i in range (12):
        if i%2:
            controle += 3* int(code[i])
        else:
            controle += int(code[i])

    controlecijf = controle % 10
    controlecijf = (10 - controlecijf) % 10
    return controlecijf == int(code[-1])

def overzicht(codes):
    groepen = {}
    for i in range (11):
        groepen [i] = 0
    for code in codes:
        if not isISBN13(code):
            groepen[10] += 1
        else:
            groepen[int(code[3])] += 1
    print(f'Engelstalige landen: {groepen[0] + groepen[1]}')
    print(f'Franstalige landen: {groepen[2]}')
    print(f'Duitstalige landen: {groepen[3]}')
    print(f'Japan: {groepen[4]}')
    print(f'Russischtalige landen: {groepen[5]}')
    print(f'China: {groepen[7]}')
    print(f'Overige landen: {groepen[6] + groepen[8] + groepen[9]}')
    print(f'Fouten: {groepen[10]}')