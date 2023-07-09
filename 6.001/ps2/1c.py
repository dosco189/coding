import string
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#letters_guessed = ['a', 'p', 'l', 'e']
letters_guessed = ['a', 'p', 'p', 'l', 'e']

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters = string.ascii_lowercase
    if i in letters_guessed: