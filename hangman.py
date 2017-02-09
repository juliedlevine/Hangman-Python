hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

#pick random word
import random
word_options = ["turtle", "computer", "button", "yellow", "apple"]
secret_word = random.choice(word_options)

#initialize game
print "Let's play hangman!"
print hangman[0]
print "_ " * len(secret_word)

#build virtual lists to compare to one another
word_list = list(secret_word)
display_list = list("_" * len(secret_word))

#set user guesses to 0
guess_count = 0

#start game loop
while guess_count < 7:
    guess = raw_input("Guess a letter: ").lower()

    #loop through each letter in the word list
    for i in range(len(word_list)):
        #if the letter at that particular index matches the user's guess:
        if word_list[i] == guess:
            #replace the display_list at the same index with the guess
            display_list[i] = guess
        #if the user enters a letter that is not in the word at all:
        elif guess not in secret_word:
            #increase the guess count and break out of the for loop to line 104
            guess_count += 1
            break

    #check for a loser, show completed hangman figure, break out of while loop
    if guess_count == 6:
        print hangman[guess_count]
        print "Sorry you got hung!"
        break

    #check for a winner, show completed work, break out of while loop
    if word_list == display_list:
        print " ".join(display_list)
        print "You won!"
        break

    #this code runs after the for loop looks for matches in the secret word
    #print the hangman figure and current display word
    print hangman[guess_count]
    print " ".join(display_list)
