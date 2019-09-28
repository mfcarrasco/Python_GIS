#HiHo Cherry0
#Calculate average turns to win a game out of 100 games of simulation
#2/13/16 Carrasco-Harris
#SCRIPT 1 incorporates printed values for each spin round for only TEN rounds (so output is shorter); SCRIPT 2 below just provides final results of turn rounds and average number of turns for 100 games (output shorter). 

#SCRIPT 1
import random #imports the random and numpy module for the functions used below
import numpy

trials = 0 #number Cherry0 winning games
turnResult = [] #list that will allow us to append how many turns each game took to later calculate an average with
while trials < 10: #while loop that will operate until 100 games have been won
    spinResult = [-1, -2, -3, -4, 2, 2, 10] #Resultant number of cherries added or removed based on game spin
    turn = 0 #the numger of spins in a game
    cherryTree = 10 #the amount of cherries on a tree
    while cherryTree > 0: #loop that will continue as long as cherries are on tree
        spinValue = random.choice(spinResult) #the number of cherries to be added/taken off depending on a randomomly chosen value from spinResult
        print "You spun", spinValue,"so adjust your cherries accordingly." # see total cherries to be added/removed per round
        cherryTree = cherryTree + spinValue # *resultant amount of cherries after adding the random amount chosen
        if cherryTree > 10:
            print "Your tree still has 10 cherries." # *
            cherryTree = 10 #the cherry tree cannot have more than ten cherries in this game
        elif cherryTree <0:
            print "Your tree has no cherries!" # *
            cherryTree = 0 # the cherry tree game is won when the user has no cherries left
        else:
            cherryTree = cherryTree
            print "You have", cherryTree,"cherries on your tree." # *
        turn += 1 #adds a turn after each spin round until game over
    print "Congratulations! You won HiHo CherryO! It took you", turn," times to win your game." #allows user to know how many turns each particular game took
    trials +=1 #adds a trial after each winning game. 
    turnResult.append(turn) #appends the number of turns it took to win a game. Must be in this line to only count the final turn number; otherwise, will append each turn to list. 
print "Here is a list of how many turns it took to win each game:", turnResult #prints the list values so user can verify number of turns per game
print "It took an average of", numpy.mean(turnResult), "turns to win." #calculates and prints out the average of turns it took to win out of all games. 


#SCRIPT 2

import random #imports the random and numpy module for the functions used below
import numpy

trials = 0 #number Cherry0 winning games
turnResult = [] #list that will allow us to append how many turns each game took to later calculate an average with
while trials < 100: #while loop that will operate until 100 games have been won
    spinResult = [-1, -2, -3, -4, 2, 2, 10] #Resultant number of cherries added or removed based on game spin
    turn = 0 #the numger of spins in a game
    cherryTree = 10 #the amount of cherries on a tree
    while cherryTree > 0: #loop that will continue as long as cherries are on tree
        spinValue = random.choice(spinResult) #the number of cherries to be added/taken off depending on a randomomly chosen value from spinResult
        cherryTree = cherryTree + spinValue # *resultant amount of cherries after adding the random amount chosen
        if cherryTree > 10:
            cherryTree = 10 #the cherry tree cannot have more than ten cherries in this game
        elif cherryTree <0:
            cherryTree = 0 # the cherry tree game is won when the user has no cherries left
        else:
            cherryTree = cherryTree
        turn += 1 #adds a turn after each spin round until game over
    trials +=1 #adds a trial after each winning game. 
    turnResult.append(turn) #appends the number of turns it took to win a game. Must be in this line to only count the final turn number; otherwise, will append each turn to list. 
print "Super! You've played 100 games. Here is a list of how many turns it took to win each game:", turnResult #prints the list values so user can verify number of turns per game
print "It took an average of", numpy.mean(turnResult), "turns to win." #calculates and prints out the average of turns it took to win out of all games. 


