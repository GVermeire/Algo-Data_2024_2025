def samenvoegen(lst1: list, lst2: list):
    rits =[]
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

