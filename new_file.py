import random
def rock_paper_scissors():
  options = ['rock', 'paper', 'scissors']
  computer_pick = random.choice(options)
  # prompt
  user_pick = input('Welcome to Rock-Paper-Scissors. Please input your choice: \n')
 # go through logic
 #logic if tie
  if computer_pick == user_pick:
   print('Tie! Both users selected ' + computer_pick)
  # logic if computer picked rock
  elif computer_pick == 'rock':
    if user_pick == 'paper':
      print('You win! ' + user_pick + ' beats ' + computer_pick)
    else:
      print('You lose! ' + computer_pick + ' beats ' + user_pick)
  # logic if computer picked paper
  elif computer_pick == 'paper':
    if user_pick == 'scissors':
      print('You win! ' + user_pick + ' beats ' + computer_pick)
    else:
      print('You lose! ' + computer_pick + ' beats ' + user_pick)
  # logic if computer picked scissors
  elif computer_pick == 'scissors':
    if user_pick == 'rock':
      print('You win! ' + user_pick + ' beats ' + computer_pick)
    else:
      print('You lose! ' + computer_pick + ' beats ' + user_pick)
rock_paper_scissors()