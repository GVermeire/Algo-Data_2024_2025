#deze oef bepaal je de excepts door allemaal errors te laten proberen plaatsvinden
numlist = [ 100, 101, 0, "103", 104 ]

try:
    i1 = int( input( "Give an index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] )

#value error, toen ik a had ingegeven als input
except ValueError:
    print("Fout: Ongeldige invoer, geef een numerieke waarde.")

#ZeroDivisionError als index 2 wordt gegeven
except ZeroDivisionError:
    print("Fout: Delen door nul is niet toegestaan.")

#Index error: als een index groter dan 4 wordt gegeven
except IndexError:
    print("Fout: Index buiten bereik.")

#TypeError: als index 3 wordt gegeven
except TypeError:
    print("Fout: Ongeldige operatie, controleer de datatypes.")