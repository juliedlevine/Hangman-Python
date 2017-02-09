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

import random
word_options = ["turtle", "computer", "button", "yellow", "apple"]
secret_word = random.choice(word_options)
print "Let's play hangman!"
print hangman[0]
print "_ " * len(secret_word)

word_list = list(secret_word)
display = list("_" * len(secret_word))

guess_count = 0

while guess_count < 7:
    guess = raw_input("Guess a letter: ").lower()

    for i in range(len(word_list)):
        if word_list[i] == guess:
            display[i] = guess
        elif guess not in secret_word:
            guess_count += 1
            break

    if guess_count == 6:
        print hangman[guess_count]
        print "Sorry you got hung!"
        guess_count += 1
        break

    if word_list == display:
        print " ".join(display)
        print "You won!"
        break

    print hangman[guess_count]
    print " ".join(display)
