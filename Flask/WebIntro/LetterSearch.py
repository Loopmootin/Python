
def search4letters(phrase : str, letters : str='aeiou') : # Defines a function
    return set(letters).intersection(set(phrase)) 