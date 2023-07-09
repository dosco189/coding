secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#letters_guessed = ['a', 'p', 'l', 'e']
letters_guessed = ['a', 'p', 'p', 'l', 'e']

def is_word_guessed(secret_word, letters_guessed):
    secret_word_list = list(secret_word)
    while len(secret_word_list) == len(letters_guessed):
        if secret_word_list == letters_guessed:
            return True
        else:
            return False
    else:
        return False
print(is_word_guessed(secret_word, letters_guessed))