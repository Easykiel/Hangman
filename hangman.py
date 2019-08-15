# This program plays the game hangman

def make_man():
    """
    Makes the initial man for Hangman
    Which is an empty string
    returns the empty string man
    """
    man = ''
    return man #returns man

def display_man(man,number_guesses):
    """
    prints man depending on number of guesses
    """
    if number_guesses == 7:# if 0 wrongs
        print()
        print(man)
        print()
    if number_guesses == 6:# if 1 wrong
        print()
        print(' | ')
        print()
    if number_guesses == 5:# if 2 wrong
        print()
        print(' | ')
        print(' 0 ')
        print()
    if number_guesses == 4:# if 3 wrong
        print()
        print(' | ')
        print(' 0 ')
        print(' | ')
        print()
    if number_guesses == 3:# if 4 wrong
        print()
        print(' | ')
        print(' 0 ')
        print('/| ')
        print()
    if number_guesses == 2:# if 5 wrong
        print()
        print(' | ')
        print(' 0 ')
        print('/|\\')
        print()
    if number_guesses == 1:# if 6 wrong
        print()
        print(' | ')
        print(' 0 ')
        print('/|\\')
        print('/')
    if number_guesses == 0:# if 7 wrong
        print()
        print(' | ')
        print(' 0 ')
        print('/|\\')
        print('/ \\')
        print()
    return

def secret(secret_word):
    """
    turns secret word into ?s
    returns the converted secret word
    """
    secret = ''

    for letter in secret_word:
        secret += '?'
        
    return secret

def display_secret(secret):
    """
    prints out secret word
    """
    print(secret)

def get_guess(guesses):
    """
    Gets the user guess
    Checks for valid input
    returns guessed letter if valid
    """
    while True:
        prompt2 = ('Please enter your next guess: ')
        guess_word = input(prompt2)
        guess_word = guess_word.split()#splits to check for spaces


        if len(guess_word) < 1:#if there is no guess
            print('You must enter a guess.')
            
        elif len(guess_word[0]) > 1:#if there are more than one character
            print('You can only guess a single character.')

        elif guess_word[0] in guesses:#if guessed already
            print('You already guessed the character:', guess_word[0])

        elif is_valid_guess(guess_word) == True:#if valid
            return guess_word[0]


def is_valid_guess(guess_word):
    """
    Checks if the letter is valid
    returns True if it is
    """
    if len(guess_word) == 1 or guess_word == '-':#if only one letter
        return True
    else:
        return False

def letters_guessed(guesses):
    """
    Prints out letters guessed
    returns letters guessed
    """
    letter_guess = ''
    guesses.sort()#sorts lists of guesses
    for letter in guesses:#adds letters in letter_guess
        if letter == guesses[-1]:#if last letter dont add comma
            letter_guess += letter
        else:#if not the last letter add a comma and space
            letter_guess += letter + ', '
    print('So far you have guessed: %s' % (letter_guess))
    return letter_guess
        
def is_guess_right(guess,secret_word):
    """
    Checks if letter guessed is in secret word
    returns True
    """
    if guess in secret_word:
        return True

def update_secret(right_guesses,secret_word):
    """
    Updates converted secret word when letter is guessed correctly
    returns secret word
    """
    secretword = ''
    for letter in secret_word:#adds the guess in secret word
        if letter in right_guesses:
            secretword += letter
        else:#adds ?s if letter not guessed yet
            secretword += '?'

    return secretword

def game_over(number_guesses,secret_word,secretword,guess_word):
    """
    Checks when game is over
    returns True or False
    """
    if number_guesses == 0:#when user runs out of guesses
        return True
    elif secretword == secret_word:#when user guesses the secret word
        return True
    else:
        return False

def win(secret_word,secretword):
    """
    checks if player wins
    returns true
    """
    if secret_word == secretword:#if secret word is the same as the guessed letters
        return True

def play_hangman():
    """
    Plays a game of hangman
    """
    prompt = ('Please enter a word to be guessed\n'
              'that does not contain ? or white space: ')

    while True:#checks for valid input
        secret_word = input(prompt)
        if '?' in secret_word:
            False
        elif ' ' in secret_word:
            False
        else:
            break

#all the things to keep track of
    secretword = secret(secret_word)
    guess_word = ''
    guesses = []
    right_guesses = []
    wrong_guesses = []
    man = make_man()
    number_guesses = 7

#while the game is playing  
    while not game_over(number_guesses,secret_word,secretword,guess_word):
        display_man(man,number_guesses)
        display_secret(secretword)
        letters_guessed(guesses)
        next_guess = get_guess(guesses)
        is_guess_right(next_guess,secret_word)
        
        if is_guess_right(next_guess,secret_word) == True:#appends the guessed letter if correct
            guesses.append(next_guess)
            right_guesses.append(next_guess)
            secretword = update_secret(right_guesses,secret_word)
        else:
            guesses.append(next_guess)
            wrong_guesses.append(next_guess)
            number_guesses = number_guesses - 1

    if win(secret_word,secretword):#when player wins
        print('You correctly guessed the secret word: %s' % (secret_word))
    else:#when player loses
        display_man(man,number_guesses)
        print('You failed to guess the secret word: %s' % (secret_word))
    
    
    
play_hangman()
