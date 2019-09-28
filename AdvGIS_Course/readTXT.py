#Parsing a text file to retrieve lat and long
#Goal: create a simple script that will allow us to create GIS files.

gps = open(r"H:\6525\mfcrrsco\gps_track.txt") #gps is now file object
headerLine = gps.readline() #headerLine is object #read line reads line by line; readlines reads all lines
print headerLine

valueList = headerLine.split(",") #built in function for string to split at commas to create a list of the words
print valueList[2]

#softcoding:
latValueIndex = valueList.index("lat")
longValueIndex = valueList.index("long")
print latValueIndex
print longValueIndex

#read lines
coord = [] #will create a nested list
for line in gps.readlines(): #lines is a counter
    segmentLine = line.split(",")
    coord.append([segmentLine[latValueIndex], [segmentLine[longValueIndex]]])
print coord

for i in coord:
    print i[0] ,",", i[1]
    

    