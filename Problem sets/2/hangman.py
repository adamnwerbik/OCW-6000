# Problem Set 2, hangman.py
# Name: Adam Werbik
# Collaborators:
# Time spent: 20 mins

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word = list(secret_word)
    gsd_word = []
    for letter in word:
      if letter not in letters_guessed:
        letter = " _ "
      gsd_word.append(letter)
    return "".join(gsd_word)

#secret_word = "apple"
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's', 'p', 'a', 'l']
#print(get_guessed_word(secret_word, letters_guessed))
#print(is_word_guessed(secret_word, letters_guessed))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters = string.ascii_lowercase
    list_available_letters = []
    for letter in list(all_letters):
      if letter not in letters_guessed:
        list_available_letters.append(letter)
      else:
        ()
    return "".join(list_available_letters)


#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']   
#print(get_available_letters(letters_guessed))
#print(get_guessed_word("billboards", ['a','l','b']))
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    guesses_left = 6
    warnings = 0
    print("Welcome to the game of Hangman!")
    print(f"The word that I'm thinking of is {len(secret_word)} letters long. \nYou have {warnings +3} warnings left \n---------------------------------")
    unique_letters = "".join(set(secret_word))
    while guesses_left > 0:
      print(f"You have {guesses_left} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      guess = input("Guess a letter: ").lower()
      #check if player entered a valid input
      if guess.lower() in string.ascii_lowercase and not guess.lower() in letters_guessed: #if valid
        letters_guessed.append(guess.lower())
        if guess in secret_word:
          if is_word_guessed(secret_word, letters_guessed):
            print(f"Congratulations! You won! \nYour total score for this game is: {guesses_left * len(unique_letters)}")
            break
          print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        else:
          print(f"Oops. That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
          if guess.lower() in ['a', 'e', 'i', 'o', 'u']:
            guesses_left -= 2
          else:
            guesses_left -= 1
          
      else:
        warnings += 1
        print(f"You must guess a letter; one that you haven't guessed yet. This is warning number {warnings} out of 3. Then you will lose a guess.")
        if warnings >= 3:
          guesses_left -= 1
    if guesses_left <= 0:
      print(f"Sorry you ran out of guesses. The word was {secret_word}")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "") #remove spaces
    if len(my_word) != len(other_word):
      return False
    for i in range(len(my_word)):
      if my_word[i] != "_":
        if my_word[i] != other_word[i]:
          return False
    return True
      

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matching_words = []
    for word in wordlist:
      if match_with_gaps(my_word, word):
        matching_words.append(word)  
    return matching_words
    # FILL IN YOUR CODE HERE AND DELETE "pass"

#print(show_possible_matches("g _ _"))
#print(show_possible_matches("t_ _ t"))

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    guesses_left = 6
    warnings = 0
    print("Welcome to the game of Hangman!")
    print(f"The word that I'm thinking of is {len(secret_word)} letters long. \nYou have {warnings +3} warnings left \n---------------------------------")
    unique_letters = "".join(set(secret_word))
    while guesses_left > 0:
      print(f"You have {guesses_left} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      guess = input("Guess a letter: ").lower()
      #check if player entered a valid input
      if guess == '*':
        print(f"Possible word matches are: {str(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))}")
      elif guess.lower() in string.ascii_lowercase and not guess.lower() in letters_guessed: #if valid
        letters_guessed.append(guess.lower())
        if guess in secret_word:
          if is_word_guessed(secret_word, letters_guessed):
            print(f"Congratulations! You won! \nYour total score for this game is: {guesses_left * len(unique_letters)}")
            break
          print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        else:
          print(f"Oops. That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
          if guess.lower() in ['a', 'e', 'i', 'o', 'u']:
            guesses_left -= 2
          else:
            guesses_left -= 1
      else:
        warnings += 1
        print(f"You must guess a letter; one that you haven't guessed yet. This is warning number {warnings} out of 3. Then you will lose a guess.")
        if warnings >= 3:
          guesses_left -= 1
    if guesses_left <= 0:
      print(f"Sorry you ran out of guesses. The word was {secret_word}")

  
# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman("secret_word")

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
