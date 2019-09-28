#HiHo Cherry-O Game Simulation
#2/10/16 - Carrasco-Harris

import random
#variable setting
cherryOntree = 10
spinOption = [-1,-2,-3,-4,2,2,10] #these are the number of cherries that are removed depending on what piece of the board you land on in the game
turn = 0
#Example: spinOption[3] would give us the value -4

while cherryOntree > 0: #so the game can continue until are the cherries are gone

    spinIndex = random.randrange(0,len(spinOption)) #the value of the index
    spinResult = spinOption[spinIndex] #variable to store the actual number of cherries that need to be taken off
    print "you spun", spinResult," so adjust your cherries accordingly"
    cherryOntree= cherryOntree + spinResult #overwrite to give the new number of cherries on tree
    if cherryOntree > 10:
        cherryOntree = 10
        print "Amount of cherries on your tree:", cherryOntree
    elif cherryOntree < 0:
        cherryOntree = 0
        print "Amount of cherries on your tree:", cherryOntree
    else:
        print "Amount of cherries on your tree:", cherryOntree
    turn +=1
print "You won! It took", turn, "times to win your game."
    
    #assignment: what is the average number of turns to win for 1,000 times game.
    #assignment: 2 - find a prime number with a while loop
