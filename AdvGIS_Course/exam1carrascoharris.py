#Exam 1 Script
#2/23/15
#Malle Carrasco-Harris

#Question 1 - Evaluating user-provided temperatures

##while True: #the loop will continue asking for a temperature
##    temp = int(input("Please enter a temperature:")) #user input of temperature that will continue to be prompted throughout loop
##    print "Please enter a temperature:", temp #statement to print before evaluation of user input
##    if temp == 0: #the way to break the loop is only if the user puts in a temperature of zero
##        print "Good bye!"
##        break #will stop the loop
##    elif temp >= 100: #temperature over OR equal to 100 are hot; temperatures under OR equal to 60 are cold. 
##        print "It is hot."
##    elif temp <= 60:
##        print "It is cold."
##    else: #temperatures that do not meet the criteria above are in between 61-99 and are just right
##        print "It is just right."
##        
#Question 2 - Evaluating 100 random numbers of range 1,1000 for number of odd and even numbers.

##import random #import random module
##even = [] #lists that will contain even or odd numbers 
##odd = []
##i = 0 #counter for while loop
##while i <100: #while loop to continue generating 100 random numbers
##    n = random.randint(1,1000) #variable that holds a random number from the random integer function 
##    if n % 2 == 0: #even numbers are divisible by 2 with no remainder
##        even.append(n) #appends the number to the even number list 
##    else: #odd numbers not divisible by 2 and leave a remainder
##        odd.append(n) #appends the number to the odd number list
##    i+= 1 #counter adds one
##
##print "Out of 100 Random Numbers,", len(even),"were even and", len(odd)," were odd." #will print out the resultant number of even numbers or odd numbers in either list using the len() function
###print even # can be uncommented to check what numbers were even or odd
###print odd

#Question 3 - Evaluate if a player loses three times in a row.

results = ['w','w','w','w','L','L','w','L','w','L','L','L','w','w','L'] #list variable

loss = 0

for value in results: #will go through all the values in list
    if value == 'L':
        loss += 1
    if value == 'w':
        loss = 0
    if loss == 3:
        print "You lost three times in a row!!" #would've been better if it was imbedded within the first if statement. 


#Kwon's method
##results = ['w','w','w','w','L','L','w','L','w','L','L','L','w','w','L'] #list variable
##
##for i in range(2, len(results)):
##    if results[i] == 'L':
##        if results[i-1] =='L': #we started with the 3rd number and worked backwards becuase end up getting out of range error if the result does not have 3 Losses
##            if results[i-2] == 'L':
##                print "You lost 3 times in a row"
##                break #break matches LOOP, it has nothing to do with the "if" statements
    