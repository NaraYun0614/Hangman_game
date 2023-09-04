def guess_and_update(word, state):
    """ Asks the user to enter a single-letter guess.
        If the guessed letter is present in word, updates state and
        returns True, otherwise returns False without updating state.
    Args:
        word (str): A word that the user is trying to guess
        state (list of str): A list of single-letter strings
    Returns: bool
    """
    guess = input("Guess a letter: ")
    found = False
    for i in range(len(word)):
        if word[i] == guess:
            state[i] = guess
            found = True
    return found

def play_game(secret_word, max_tries):
    """ Plays the guessing game of Hangman.
    Args:
        secret_word (str): Secret word that user will try to guess
        max_tries (int):   Max no. of incorrect tries before stopping the game
    Returns: None
    """
    game_state = []
    for i in range(len(secret_word)):   #add # of '_' using the length of secret_word
        game_state.append('_')

    attempt = 0 # count # of attempt
    while attempt < max_tries: 
        print(" ".join(game_state))  # print game_state wwith the spaces
        result = guess_and_update(secret_word, game_state)   # calling the above function for asking input and update game_state
        if result == False:
            attempt += 1
            print("Incorrect! # of tries:", attempt)  # add # of incorrect attempt
            
        elif result == True and '_' not in game_state: # success to guess the word
            print(" ".join(game_state))  # print current state
            print("Congrats, you won!")  
            break  # to print the message one time only

        else:   # when letter guess is correct but not get all the correct word
            continue    

    if attempt >= max_tries:
        print("Sorry, you lose.")
   

# test cases inside this if-statement
if __name__ == "__main__":  
    # Example 1:
     play_game("common", 5)
    
    # Example 2:
    # play_game("common", 4)
    
    # Example 3:
    # play_game("python", 2)
    
    # Example 4:
    # play_game("cat", 3)