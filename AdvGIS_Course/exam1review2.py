#test practice 2/20/16
#1. Make sure you first review all .pdf files uploaded.
##Try following five exercises until you get it work without any help:


#Rock, Paper, Scissors - (advanced: Try game ends when you lose three times in a row)

import random
##plays = ["R","P","S"]
##games = 0
##
##print "Welcome to Rock, Paper, Scissors."
##while games < 3:
##    user = str(raw_input("What's your play? \n R,P,S: "))
##    comp = random.choice(plays)
##    print "You chose:", user
##    print "The computer chose:", comp
##    if user == comp:
##        print "It's tied!"
##        games = 0
##    elif (user,comp) in [("R", "S"), ("P","R"), ("S","P")]:
##        print "You win this game!"
##        games = 0
##    else:
##        print "You lost this game."
##        games +=1
##print "Sorry you lost", games, "games."
 

#Beatle's listing

##members = ["MF", "KD", "RR", "JJ"]
##order = ["First","Second", "Third", "Fourth"]
##punc = [",", ",",",","."]
##
##for i in range(4):
##    print "The", order[i], "member is", members[i], punc[i]

#Grade Calculator
##import random
##print "Welcome to the Grade Calculator."
##randomgrade = random.randint(0,100)
##num = randomgrade
##print num
##if num >= 90:
##    print "Your letter grade is an A"
##elif num >= 80:
##    print "Your letter grade is a B"
##elif num >= 70:
##    print "Your letter grade is a C"
##elif num >= 60:
##    print "Your letter grade is a D"
##else:
##    print "Your letter grade is an F"

    
#CherryO game (calculate average turn to win when you do 100 games)
##import random
##spinOptions = [-1,-2,-3,-4, 2, 2, 10]
##games = 0
##listTurns = []
##
##while games < 100:
##    cherries = 10
##    turns = 0
##    #print "You start with 10 cherries."
##    while cherries > 0:
##        spin = random.choice(spinOptions)
##        #print "You spun", spin
##        if (cherries + spin) > 10:
##            cherries = 10
##            #print "You have", cherries," cherries on your tree."
##        elif (cherries + spin) <= 0:
##            cherries = 0
##            #print "You have", cherries,"left and you win."
##        else:
##            cherries = cherries + spin
##            #print "You have", cherries,"left."
##        turns  += 1
##    games += 1
##    listTurns.append(turns)
##    #print "It took you", turns," turns to win the game."
##print "Here are how many turns it took for each game", listTurns
##print "You played", games," games."
##print "The average number of turns it took to win each game is", float((sum(listTurns))/games)

#Find prime number (using both while loop and for loop, with user input upto number)
#while loop
#work on this one again

##x = 2
##upTo = int(input("To what number do you want to count the primes?:"))
##prime = []
##while x <= upTo:
##    j = 2
##    while j < x:
##        if x % j == 0:
##            break
##        j +=1    
##    else:
##        print "%d is a prime number" % (x)
##        prime.append(x)
##    x +=1
##print "There are", len(prime),"prime numbers up to", upTo

#for loop

##upTo = int(input("To what number do you want to count the primes?:"))
##prime = []
##for n in range(2, upTo):
##    for i in range(2, n):
##        if n % i == 0:
##            break
##        i += 1
##    else:
##        print "%d is a prime number" % (n)
##        prime.append(n)
##    n += 1
##print "There are", len(prime),"prime numbers up to", upTo

#Factorial calculation (using both while loop and for loop)       
 #practice this one again       
##num = int(input("Type in number for n!:"))
##i = 1
##x = num
##while i < num:
##    x = x * i
##    i += 1
##print "The factorial of",num,"is", x

#for loop

##num = int(input("Type in number for \n n!:"))
##x = num
##for i in range(1,num):
##    x = x * i
##print "The factorial of", num,"is",x

#Guess the number (using both for loop and while loop)
#while loop
##import random
##comp = random.randint(1,20)
##user = int(input("Guess a number between 1 and 20:"))
##try:
##    while True: 
##        if user > comp:
##            user = int(input("Too high, try again:"))
##        elif user < comp:
##            user = int(input("Too low, try again:"))
##        elif user == comp:
##            print "You got it!"
##            break
##except:
##    print "You stopped playing"

#for loop
##print "You have three tries to guess correctly"
##import random
##comp = random.randint(1,20)
##user = int(input("Guess a number between 1 and 20:"))
##i = 1
##for i in range(1,3):
##    print "your choice was:", user
##    if user > comp:
##        user = int(input("Too high, try again:"))
##    elif user < comp:
##        user = int(input("Too low, try again:"))
##    elif user == comp:
##        print "You got it!"
##        break
##    i += 1
##if user == comp:
##    print "you won"
##else:
##    print "You lose; your choise was:", user,"\n the correct number was:",comp

#Find prime number (using both while loop and for loop, with user input upto number)

upTo = int(input("Find primes up to:"))

list = []
n = 2
while n <= upTo:
    i = 2
    while i < upTo:
        if n % i == 0:
            break
        i +=1
    else:
        print "%d is a prime number." % (n)
        list.append(n)
    n += 1
print "The list of prime numbers up to", upTo,"is", list
print "There are", len(list),"prime numbers up to", upTo