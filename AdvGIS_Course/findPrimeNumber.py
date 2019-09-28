#find a prime number
#2/11/16 - Carrasco-Harris


for i in range(2,11): #evalutate number 11 (hard coding number example)
    if 11 % i == 0:
        print "11 is not a prime number"
print "11 is prime number"
        

for i in range(2,10): #evalutate number 10 (hard coding number example)
    if 10 % i == 0:
        print "10 is not a prime number"
        break
else:
    print "10 is prime number"


#Soft coding:
for num in range(10,21):
    for i in range(2,num):
        if num % i == 0:
            print num," is NOT a prime number"
            break
    else:
        print num," is prime number"

#count how many prime numbers in between 2 and 100.
count = []
for num in range(2,101):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        count.append(num)
print "there are a total of", len(count), "prime numbers"


#User input of range

upTo= int(raw_input("up to numbers: "))
count = []
for num in range(2,upTo):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        count.append(num)
print "there are a total of", len(count), "prime numbers"

  
    