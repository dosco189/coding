secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#letters_guessed = ['a', 'p', 'l', 'e']
letters_guessed = ['a', 'p', 'p', 'l', 'e']

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_word_list = list(secret_word)
    return_guess = []
    for i in secret_word_list:
        if i in letters_guessed:
            return_guess.append(i)
        else:
            return_guess.append('_ ')
    return ''.join(return_guess)

print(get_guessed_word(secret_word, letters_guessed))   