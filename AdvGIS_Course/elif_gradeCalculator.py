#if-elif-else statement
#2/3/16 by malle

#variable setting - user supplied score

score = int(raw_input("type your score here: "))
words ="Your letter grade is "
letterGrade = ["A","B","C","F"] #moved on to change the lines below, also. Did not complete this

if score >= 90:
    print words + "A"
elif score >= 80:
    print words + "B"
elif score >= 70:
    print words + "C"
else:
    print words + "F"
print "Done!"
