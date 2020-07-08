import random
def hangman_game():
  # list of words to coose from
  word_list = ["hello", "goodbye", "desk", "age", "sunny", "excellent", "bear", "paw"]
  # select random word from list
  word = random.choice(word_list)
  word_length = len(word)
  # welcome message
  print('Welcome to Hangman! The word is ' + str(word_length) + ' letters.  Guess a letter:')
  incorrect_count = 0
  correct_count = 0
  i = 0
  # adds  guesses to a string
  guesses = ''
  blank_count = len(word)
  new_word = ''
  # prompt input when less than 7 wrong guesses and when user has not completed the word
  while incorrect_count < 7 and new_word != word:
    new_word = ''
    # new_word stores all correctly guessed letters. logic follows
    for char in word: 
      if char in guesses:
        new_word += char
      else:
        new_word += '-'
    if incorrect_count >= 6:
      print('Too many incorrect guesses. Game over.')
    if new_word == word:
      print('Good job! You guessed the word: ' + word)
    else:
      print('Current status: ' + new_word)
    # print('blanks: ' + str(blank_count))
      print('Incorrect guesses: ' + str(incorrect_count))
    c = input()
    guesses += c
    if c not in word:
        incorrect_count += 1
  return
hangman_game()