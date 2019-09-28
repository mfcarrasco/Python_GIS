#Rock paper scissors
print "Let's play Rock, Paper, Scissors.Rock is R, Paper is P, and Scissors is R"
choices = ["R", "P", "S"]
i= 0
j = 0
try:
    while i <5:
            user = str(raw_input("Your choice \n R, P, S:"))
            comp = random.choice(choices)
            print "user" ,user
            print "comp" ,comp
            if user == "R" and comp == "P":
                print "You chose", user,"and comp chose", comp,"and wins."
            elif user == "P" and comp == "S": #can also use or statements to condense and have one 
                print "You chose", user,"and comp chose", comp,"and wins."
            elif user == "S" and comp == "R":
                print "You chose", user,"and comp chose", comp,"and wins."
            elif user == comp:
                print "Comp chose",comp,"and you chose", user," There's a tie"
            else:
                print "Comp chose", comp, "and you win with", user,"."
                j +=1
            i += 1
    print "You won" ,j, "games out of 5."
except:
    print "You stopped playing."


#elif (player == 'R' and com == 'S')\
    #or (player == 'P' and com == "R")\
    #or ((player == "S" and com == "P"):
        #print "player win"

# elif (player, com) in [('R','S'), ('P',"R"), ("S", "P")]:
    #print "player win"
    