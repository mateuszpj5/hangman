from random import choice

words = ["phalange", "umbrella", "palantiri"]
hangman_art = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']


print("Welcome to the game!\n" + hangman_art)
the_word = choice(words)
# print(the_word)
display = []
for i in range(len(the_word)):
  display.append("_")
print(*display)  
the_end = False
lives = 7
letters_used = []
while not the_end:
  guess = input("Take a guess: ")
  if letters_used.count(guess) == 0:
    letters_used.append(guess)
    for i in range(len(the_word)):
      if the_word[i] == guess:
        display[i] = guess
    print(*display)
    if display.count(guess) == 0:
      lives -= 1
      print(stages[lives])
    if lives < 1:
      the_end = True
      print("You lost!\nGAME OVER!")
    elif display.count("_") == 0:
      the_end = True
      print("You won!\nGAME OVER!")
  else:
    print("The letter was already used! Try again!")