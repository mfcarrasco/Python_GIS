#Create a script to remove duplicates from a list
#Exercise 3 in Ch. 4

print "next trial"
mylist = [1,4,87,9,99,84,22,4,65,22,7,9]
for number in mylist:
    count = mylist.count(number)
    if count <> 1:
        print "The list contains duplicate values of", number
        mylist.remove(number)
    else:
        print "the list does not contain duplicate values of", number
print mylist
