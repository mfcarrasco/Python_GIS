#Find prime numbers by using user input and while loop.
#2/13/16 - Carrasco-Harris

upTo = int(input("Type number here: ")) #This codes for the users input
count = [] #This is a LIST that will allow me to know at the end how many numbers are prime
i = 2 #Start number (starting with 1 will give 1 as a false prime number). 
while i <= upTo: #This loop will run until the inputed range value upTo is reached
    j = 2 #This will be our dividing factor to determine if a number is prime
    while j < i: #this nested while loop will run while the dividing factor is still less than the range input value
        if (i%j) == 0: #if the the remainder is zero, then the number is NOT a prime number 
            break #break this loop and go back to the second while to increase the factor j
        j += 1 
    else: #if the above statement is not true, and there is a remainder for all divided factors, the loop will continue here.
        print i," is a prime number"
        count.append(i) #the append function will add the current "i" to the list.
    i += 1
print "There are", len(count), "prime numbers up in your range up to", upTo,"." #len() gives the length of the list Count 