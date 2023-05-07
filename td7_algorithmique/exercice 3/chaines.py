def frequences(mot):
    """
    Retourne un dictionnaire avec les lettres du mot et leur nombre d'apparition
    """
    freq = {}
    for lettre in mot:
        if lettre in freq:
            freq[lettre] += 1
        else:
            freq[lettre] = 1
    return freq
