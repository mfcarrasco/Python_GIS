
# Calculate the average spins to win a 'Hi Ho Cheery O' game out of 100 plays 
# ESCI 6525 Advanced GIS Assignment 3-2

import random

# Variable setting
cherryOntree = 10 # Cherrys on the tree in the beginning  
spinOption = [-1,-2,-3,-4,2,2,10]
gameTime = 0 # Play times
spinTime = 0 # Spin times per play
totalSpinTime = 0 # Spin times in total play
for gameTime in range(0,101):
    while cherryOntree > 0:
        print "Initial cherry right after while loop", cherryOntree #WE USED THIS PRINT STATEMENT TO DEBUG
        spinIndex = random.randrange(0,len(spinOption)) # spin the spinner
        spinResult = spinOption[spinIndex] #spin result
        print "sprin result", spinResult #WE USED THIS PRINT STATEMENT TO DEBUG
        cherryOntree = cherryOntree + spinResult # cherries on the tree after spinning
        print "cherry after the spin", cherryOntree #WE USED THIS PRINT STATEMENT TO DEBUG
        if cherryOntree >= 10:
            spinTime += 1 # count on this spin
            cherryOntree = 10 # reset 10 cheeries on the tree if there are more than 10 cheeries 
        elif (cherryOntree < 10) and (cherryOntree > 0):
            spinTime += 1 # count on this spin
        else:
            spinTime += 1 # count on this spin
            cherryOntree = 10 # win the game and reset 10 cherries on the tree 
            gameTime += 1 # move to next play
            totalSpinTime += spinTime # count total spin times in all plays
            print 'Game', gameTime-1, ', You span', spinTime, 'times to win the game.'
            break
    spinTime = 0
averageSpinTime = (float(format(totalSpinTime, '.2f')))/100 # calculate the average spins per game to win the game
print 'Hi Ho Cheery O! You have span', totalSpinTime, 'times in', gameTime-1, 'plays. Predictably, you should play', averageSpinTime, "times to win the 'Hi Ho Cheery O' game."