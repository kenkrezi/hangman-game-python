# import additional functions
from random import choice   # function choice - selects random item from the list
from IPython.display import clear_output   #jupyter notebook specific function which clears oputput

# declare game variables
words = [ "tree", "basket", "chair", "paper", "python"]
word = choice(words)   # randomly chooses a word from the list
guessed, lives, game_over = [], 7, False    # multivariable assignment

# create a list of underscores to the length of the word
guesses = [ "_ " ] *len(word)   # list of underscores equal to the length of the word chosen

# create the main loop
while not game_over:
    ans = input("Type quit or guess a letter: ").lower() 
    # Outputting Game Information
    hidden_word = "".join(guesses)  # join method - joins all items within guesses list together with no spacesin btwn
    print("Word to guess: {}".format(hidden_word))
    print("Lives: {}".format(lives))
    clear_output()
    if ans == "quit":
        print("Thanks for playing.")
        game_over = True
    
    elif ans in word:  # check if letter in word
        print("You guessed correctly!")
        # create a loop to change underscore to proper letters
        for i in range(len(word)):
            if word [i] == ans:  # compares values at indexes
                guesses[i] = ans
    else:
        lives -= 1
        print("Incorrect, you lost a life.")
        print("Word to guess: {}".format(hidden_word))
        
        
        if lives<= 0:
            print("You lost all your lives, you lost, YOU LOST!")    
            game_over = True