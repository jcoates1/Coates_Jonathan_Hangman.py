from random import choice

#title
print("Jonathan Coates Hangman Game")

#random word selection from preset list
word = choice(["rarely", "universe", "notice", "sugar", "interference", "constitution", "we", "minus", "breath", "clarify", "take", "recording", "amendment", "hut", "tip", "logical", "cast", "title", "brief", "none", "relative", "recently", "detail", "port", "such", "complex", "bath", "soul", "holder", "pleasant", "buy", "federal", "lay", "currently", "saint", "for", "simple", "deliberately", "means", "peace", "prove", "sexual", "chief", "department", "bear", "injection", "off", "son", "reflect", "fast", "ago", "education", "prison", "birthday", "variation", "exactly", "expect", "engine", "difficulty", "apply", "hero", "contemporary", "that", "surprised", "fear", "convert", "daily", "yours", "pace", "shot", "income", "democracy", "albeit", "genuinely", "commit", "caution", "try", "membership", "elderly", "enjoy", "pet", "detective", "powerful", "argue", "escape", "timetable", "proceeding", "sector", "cattle", "dissolve", "suddenly", "teach", "spring", "negotiation", "solid", "seek", "enough", "surface", "small", "small", ])

#empty lists for incorrect letters and correct ('guessed') letters
incorrect = []
correct = []

#how many lives player gets (7 for assessment)
lives = 7

#whilst player has attempts remaining
while lives > 0:

#set 'out' to an empty string 
  out = ""
  
#forloop which adds '*' or 'letter' to 'out' string if guess incorrect or correct respectively
  for letter in word: 
    if letter in correct:
      out = out + letter
    else:
      out = out + "*"

#if word completed, stop iterations
  if out == word:
    break

#display to player - incorrect guesses, word guessed so far, request for next guess, attempts left
  print("Incorrect guesses so far: ", incorrect)
  print(out)
  print("Please enter your next guess: ")
  print(lives, "lives left")

#inputted value is guess
  guess = input().lower()

#if already guessed, display 'Already guessed'
  if guess in correct or guess in incorrect:
    print("Already guessed", guess)
#otherwise add to correctly guessed list if correct and display 'Correct'
  elif guess in word:
    print("Correct")  
    correct.append(guess)
#or add to the incorrectly guessed list if incorrect, display 'Try again' and minus a life
  else:
    print("Try again")
    lives = lives - 1
    incorrect.append(guess)  

#display a space
  print()

#display result
if lives:
  print("Congratulations you win")
else:
  print("You lose")
  
print("The word was", word)
