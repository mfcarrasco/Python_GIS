#Practice 3/3/16
#Malle Carrasco-Harris

#Practicing creating modules and functions

##def areaCircle(radius): #This defines hte function; radius is the parameter
##    area = 3.14159 * radius**2 #** is for multiplying by the following power
##    return area #return statement of the value of the value of the completed function; assign the returned value to a variable to use it later in the code. 
##
##circleArea = areaCircle(12) #assign the return value to a variable to call later in the script 
##print circleArea

##def getCurrentPresident():
##    return "Barack Obama"
##
##president = getCurrentPresident()
##print president

##def cherryO():
##    import random #imports the random and numpy module for the functions used below
##    import numpy
##
##    trials = 0 #number Cherry0 winning games
##    turnResult = [] #list that will allow us to append how many turns each game took to later calculate an average with
##    while trials < 100: #while loop that will operate until 100 games have been won
##        spinResult = [-1, -2, -3, -4, 2, 2, 10] #Resultant number of cherries added or removed based on game spin
##        turn = 0 #the numger of spins in a game
##        cherryTree = 10 #the amount of cherries on a tree
##        while cherryTree > 0: #loop that will continue as long as cherries are on tree
##            spinValue = random.choice(spinResult) #the number of cherries to be added/taken off depending on a randomomly chosen value from spinResult
##            cherryTree = cherryTree + spinValue # *resultant amount of cherries after adding the random amount chosen
##            if cherryTree > 10:
##                cherryTree = 10 #the cherry tree cannot have more than ten cherries in this game
##            elif cherryTree <0:
##                cherryTree = 0 # the cherry tree game is won when the user has no cherries left
##            else:
##                cherryTree = cherryTree
##            turn += 1 #adds a turn after each spin round until game over
##        trials +=1 #adds a trial after each winning game. 
##        turnResult.append(turn) #appends the number of turns it took to win a game. Must be in this line to only count the final turn number; otherwise, will append each turn to list. 
##    return turnResult
##import numpy
##turnResult = cherryO()
##
##print "Super! You've played 100 games. Here is a list of how many turns it took to win each game:", turnResult #prints the list values so user can verify number of turns per game
##print "It took an average of", numpy.mean(turnResult), "turns to win." #calculates and prints out the average of turns it took to win out of all games. 

#This cherryO script requires the user to input how many games of cherryO to play. 
##def cherryO(numGames):
##    import random #imports the random and numpy module for the functions used below
##    
##    trials = 0 #number Cherry0 winning games
##    turnResult = [] #list that will allow us to append how many turns each game took to later calculate an average with
##    while trials < numGames: #while loop that will operate until 100 games have been won
##        spinResult = [-1, -2, -3, -4, 2, 2, 10] #Resultant number of cherries added or removed based on game spin
##        turn = 0 #the numger of spins in a game
##        cherryTree = 10 #the amount of cherries on a tree
##        while cherryTree > 0: #loop that will continue as long as cherries are on tree
##            spinValue = random.choice(spinResult) #the number of cherries to be added/taken off depending on a randomomly chosen value from spinResult
##            cherryTree = cherryTree + spinValue # *resultant amount of cherries after adding the random amount chosen
##            if cherryTree > 10:
##                cherryTree = 10 #the cherry tree cannot have more than ten cherries in this game
##            elif cherryTree <0:
##                cherryTree = 0 # the cherry tree game is won when the user has no cherries left
##            else:
##                cherryTree = cherryTree
##            turn += 1 #adds a turn after each spin round until game over
##        trials +=1 #adds a trial after each winning game. 
##        turnResult.append(turn) #appends the number of turns it took to win a game. Must be in this line to only count the final turn number; otherwise, will append each turn to list. 
##    return turnResult
##import numpy
##turnResult = cherryO(6)
##
##print "Super! You've played 100 games. Here is a list of how many turns it took to win each game:", turnResult #prints the list values so user can verify number of turns per game
##print "It took an average of", numpy.mean(turnResult), "turns to win." #calculates and prints out the average of turns it took to win out of all games. 

#Exam average calculator: User provide test scores to calculate an exam average until they stop providing scores.

##testList = []
##while True:
##    try:
##        num = int(input("Type in an exam score here:"))
##        testList.append(num)
##        print "Your exam average for your exams", testList,"is", float(sum(testList)/len(testList)),"."
##    except KeyboardInterrupt:
##        print "You stopped adding scores. Thank you for using the exam average calculator"
##        break

#Running pace calculator for men or women ages 18-34 

miles = input("How many miles did you run?:")
time = input("How many minutes did it take you to run that many miles?:")
pace = (float(time))/miles
marTime = (26.2 * pace)/60

print "Your average pace is", pace,". \n At that pace, you would be able to finish a 26.2 miles marathon in", round(marTime,2)," hours."

gender = str(raw_input("Are you M or F?:"))

if gender == "M":
    print "error"
    if pace > 7.05:
        print "You would probably not be able to qualify for the Boston Marathon."
    else:
        print "You could qualify for the Boston Marathon!"
elif gender == "F":
    if pace > 8.2:
        print "You would probably not be able to qualify for the Boston Marathon."
    else:
        print "You could qualify for the Boston Marathon!"

else:
    print "Error in selecting M or F"



