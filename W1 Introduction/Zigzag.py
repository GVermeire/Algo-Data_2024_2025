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


def zigzag_traag(lst):
    """Zigzag-sorteert de lijst met de trage methode."""
    # Stap 1: Sorteer de lijst
    lst.sort()

    # Stap 2: Wissel elk paar opeenvolgende elementen
    for i in range(1, len(lst), 2):
        lst[i - 1], lst[i] = lst[i], lst[i - 1]
        """Links van het = teken: lst[i - 1], lst[i]
        Dit geeft aan dat we de waarde van lst[i - 1] en lst[i] willen veranderen.
        Rechts van het = teken: lst[i], lst[i - 1]"""


def zigzag_snel(lst):
    """Zigzag-sorteert de lijst met de snelle methode."""
    for i in range(len(lst)):
        if i % 2 == 0:  # even index
            if i > 0 and lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
            if i < len(lst) - 1 and lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]