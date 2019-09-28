#Exam 1 Review Exercises
#2/16/16
#Malle Carrasco-Harris

#Question 1:

mylist = ["Athens", "Barcelona", "Cairo", "Florence", "Helsinki"]

print len(mylist) #length of list = 5

print mylist[2] #index: "Cairo"

print mylist[1] #index: "Barcelona"

print mylist.index("Cairo") #index number 2

print mylist.pop(1) #will remove "Barcelona"

mylist = ["Athens", "Barcelona", "Cairo", "Florence", "Helsinki"]

mylist.sort(reverse = True) #mylist = ["Helsinki", "Florence", "Cairo", "Barcelona", "Athens"]; must have Boolean value 
print mylist #to show the list is reversed

mylist = ["Athens", "Barcelona", "Cairo", "Florence", "Helsinki"]

mylist.append("Berlin") # will add "Berlin" to the end of the list
print mylist # to show addition of Berlin to list

#Question 2

mylist = [2,5,7,23,53,11,4,6,20]

mylist.sort() #will sort list from smallest to largest number
print "The second largest number in your list is", mylist[-2], "." #will print second to last indexed number

#Question 3

num = int(input("Please pick any number on the number scale:")) #user input of number
print "The absolute value of your number is", abs(num),"." #returns the abs value of number

#Question 4       

num = int(input("Please pick a whole number:")) #user input of number

if num % 2 == 0:#even numbers yield no remainder when divided by zero
    print num,"is an EVEN number."
else:
    print num,"is an ODD number."

#Question 5


import numpy #this module will provide the average function. 
print "This program will take several numbers, then average them."
num = (input("How many numbers would you like to sum:")) #the users first input to determine number of times loop runs
i = 0 #counter
list = [] #list storage for future inputs to be averaged

while i < num: #loop that will continue until users desired amount of numbers is provided based on first input question
    j = input("Enter a number:") #user input for numbers that will be averaged
    print "Enter a number", j
    list.append(j) #adding input numbers to list to be averaged later
    i += 1
print "The average was:", round(numpy.average(list),2) #numpy function provides average of all numbers appended to list, and then round function will provide two decimal places as shown in example.

#Question 6 

import numpy
print "Welcome to the Average Calculator, please insert a number."
list = []
inf = 1

while inf == 1: #this is an infinite loop that will run until the user keyboard cancels by not inputting a number
    num = input("Enter a new number:")
    print "New number:", num
    list.append(num)
    print "The current average is", numpy.average(list)

#Question 7

import math
num = input("Enter your number:")
print "Enter your number:", num
fact = math.factorial(num)
print "The factorial of %d is %d" % (num, fact)
    

#Question 8
#lists of members and number ranks
beatles = ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"]
num = ["First", "Second", "Third", "Fourth"]
while len(beatles) > 0: #loops until list has no more members
    for value in num:
        print num[0],"Beatles member name is", beatles[0],"," #prints the first indexed value of either list
        del num[0] #deletes the first indexed value after it has been used
        del beatles[0] # " " 
    
 
#Question 9

import random
random = random.randint(0,100)

if random >= 90:
    print "Your score is", random," and your letter grade is A."
elif random >= 80:
    print "Your score is", random," and your letter grade is B."
elif random >=70:
    print "Your score is", random," and your letter grade is C."
elif random >= 60: 
    print "Your score is", random," and your letter grade is D."
else:
    print "Your score is", random,"and your letter grade is F."

