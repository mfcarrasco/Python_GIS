#Guess the number
# 2/16/16 Carrasco-Harris
# My script
import random

tries = 0
compNumb = random.randrange(1,21)

while tries < 5:
    yourNum = int(input("Guess a number between 1-20:"))
    if yourNum == compNumb:
        break
    elif yourNum < compNumb:
        tries += 1
        print "You guessed", yourNum," and is too low. Guess again. You  have", 5-tries, "turns remaing."
    else:
        tries += 1
        print "You guessed", yourNum,"and is too high. Try again, you have", 5-tries, "turns remaining."
if yourNum == compNumb:
    print "Congrats, you guess correctly"
else: print "I'm sorry, you did not guess correctly and are out of turns. You lose. The random number was", compNumb, "."

#Kwon's script

import random
num = random.randrange(1,21)

guess = int(raw_input("guess the number!: "))

turn = 0

while turn < 5:
    if guess > num:
        guess = int(raw_input("your guess is too high, guess again:"))
    elif guess < num:
        guess = int(raw_input("your guess is too low. guess again:"))
    elif guess == num:
        print "you got it!"
        break
    turn += 1
if guess == num:
    print "you won"
else:
    print "you lose"