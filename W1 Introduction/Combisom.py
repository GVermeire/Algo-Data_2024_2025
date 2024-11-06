# volgende is eig nie efficient voor grote lijsten
def combisom(lst:list, x:int):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] + lst[j] == x:
                return True
            else:
                continue
    return False


#Foute oplossing maar zie toch waar mijn fout zit, uitleg eronder
#def Combisom(lst, som):

    #for i in lst:
        #for b in lst:
            #if som == lst[i] + lst[b]:
                #return True
    #return False

#Fout 1
#Dubbele berekeningen en optellen van hetzelfde element:
#De huidige code somt elk element in de lijst met elk ander element, inclusief zichzelf. Dit betekent dat bijvoorbeeld lst[2] + lst[2] ook wordt gecontroleerd. Als je wilt voorkomen dat je hetzelfde element twee keer gebruikt, moet je ervoor zorgen dat je de tweede lus pas begint bij het volgende element in de lijst.

#Fout 2
#Gebruik van i en b als elementen, niet indexen:
#In je for-lus gebruik je i en b als elementen van de lijst, niet als indexen. Wanneer je vervolgens probeert lst[i] en lst[b] te gebruiken, krijg je een fout omdat i en b al de elementen zelf zijn, niet de indexen.
#Oplossing: Je hoeft de elementen niet nogmaals uit de lijst te halen. Je kunt direct i en b optellen.


