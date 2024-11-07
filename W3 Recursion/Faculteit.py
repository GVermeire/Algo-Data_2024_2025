def faculteit(n):
    if n > 13:
        return "invoer te groot"
    elif n==0:
        return 1
    else:
        return n*faculteit(n-1)
aantalkeer=int(input(""))
for x in range(aantalkeer):
    print(faculteit(int(input(""))))