def iszigzag(zigzag: list):
    for i in range(len(zigzag)-1):
        if zigzag[i] > zigzag[i+1] and zigzag[i+1] < zigzag[i+2]:
            return True
        else:
            return False

# print(iszigzag([2, 1, 10, 5, 49, 23, 90])) #gesorteerde lijst
# print(iszigzag( [10, 90, 49, 2, 1, 5, 23])) #ongesorteerde lijst
# True and False

def iszigzag(seq):
    """Controleert of de gegeven reeks zigzag-gesorteerd is."""
    for i in range(len(seq) - 1):
        if i % 2 == 0:  # even index
            if not (seq[i] >= seq[i + 1]):  # moet groter of gelijk zijn aan volgende
                return False
        else:  # oneven index
            if not (seq[i] <= seq[i + 1]):  # moet kleiner of gelijk zijn aan volgende
                return False
    return True