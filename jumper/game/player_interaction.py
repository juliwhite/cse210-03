
#starting off with simple rules and greetings
print("Welcome to JUMPER!")
print("Would you like to play?")
play = input("(y/n): ").lower()
while play != 'y' and play != 'n':
  print("Sorry, please pick one of the options.")
  play = input("(y/n): ").lower()
if play == 'y':
  print("Wonderful!")
elif play == 'n':
  print("Sorry to hear that. Press 'enter' to exit.")
  input(" ")
  exit()

print("Would you like to hear the rules of the game?")
rules = input("(y/n): ").lower()
while rules != 'y' and rules != 'n':
  print("Sorry, please pick one of the options.")
  rules = input("(y/n): ").lower()
if rules == 'y':
  print("RULES:")
  print("There is a man (or... jumper) who has leapt out of an airplane, and is now using a parachute to get down.")
  print("Your job is to figure out the secret word by guessing the letters in the word.")
  print("If the guess is correct, the letter is revealed.")
  print("If the guess is incorrect, a line is cut on the man's parachute.")
  print(" ")
  print("If the man's parachute disappears before the word is guessed, you lose.")
  print("If you guess the word before the parachute disappears, you WIN!")
  print("Press 'enter' when you feel you are ready to begin.")
  input(" ")
elif rules == 'n':
  print("Right to it then! Press 'enter' to begin.")
  input(" ")
