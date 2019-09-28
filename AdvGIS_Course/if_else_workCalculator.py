#working hours
#2/3/16 by Malle

towork = int(raw_input("How many hours can you work this week?: "))
#user supplied hours to work
worked = int(raw_input("How many hours have you worked this week?: "))
#user supplied hours worked

if worked > towork:
    print "Please enjoy " + str(worked-towork) + " hour(s) of vacation next week!"
elif worked == towork:
    print "You have fulfilled your work hours this week."
else:
    print "You still need to work " + str(towork-worked) + " more hour(s) this week."
    
