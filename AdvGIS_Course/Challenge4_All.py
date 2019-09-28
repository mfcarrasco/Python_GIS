#Challenge exercises 3/3/16
#Malle Carrasco-Harris

#Challenge question 1

##text = "Geographic Information Systems"
##
##if text.find("z") == -1:
##    print "No, that letter is not present"
##else:
##print "Yes, that letter is present"

#Challenge question 2

##list = [2,8,64,16,32,4,85]
##list.sort()
###print list Can print if want to verify that list was sorted correctly
##print list[-2]

#Challenge question 3

##list = [2, 8, 64, 16, 32, 4, 16, 8]
##print list
##for num in list:
##    if list.count(num) > 1:
##        print "This list contains duplicate values of", num
##        list.remove(num)
##else:
##    print "There are no duplicates."
##
##print list

#Challenge question 4

##mylist = ["Athens", "Barcelona", "Cairo", "Florence", "Helsinki"]
##
##print len(mylist) #there are 5 items in this list
##
##print mylist[2] #Cairo
##
##print mylist[1] #Barcelona
##
##print mylist.index("Cairo") #index # 2
##
##print mylist.pop(1) #will remove and return "Barcelona"
##
##mylist = ["Athens", "Barcelona", "Cairo", "Florence", "Helsinki"]
##
##mylist.sort(reverse = True) #mylist = ["Helsinki", "Florence", "Cairo", "Barcelona", "Athens"]; must have Boolean value; mylist.reverse() would also produce same result
##print mylist #to show the list is reversed 
##
##mylist = ["Athens", "Barcelona", "Cairo", "Florence", "Helsinki"]
##
##mylist.append("Berlin") # will add "Berlin" to the end of the list
##print mylist # to show addition of Berlin to list