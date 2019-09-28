#if-else statement for grade calculator:
#2/3/2016 by Malle

#variable setting - user supplied score
score = float(raw_input("type your score here: ")) #score can be a float or integer and it will work; if variable assigned as an int then float can not be used
if score >= 90:
    print "Your letter grade is A"
else:
    if score >= 80:
        print "Your letter grade is B"
    else:
        if score >= 70:
            print "Your letter grade is C"
        else:
            if score <70:
                print "Your letter grade is F"
