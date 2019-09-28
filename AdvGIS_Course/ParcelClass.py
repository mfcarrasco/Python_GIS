#Parcel Class
# 3/18/16
# Malle Carrasco-Harris

##class Parcel: #this is the class; created using class keyword
##    def __init__(self, landuse, value): #__init__ and assessment are METHODS; __init__ initializing objects --> constructing objects before they can be used
##        self.landuse = landuse
##        self.value = value
##    def assessment(self):
##        if self.landuse == "SFR":
##            rate = 0.05
##        elif self.landuse == "MFR":
##            rate = 0.04
##        else:
##            rate = 0.02
##        assessment = self.value * rate
##        return assessment
##
##myparcel = Parcel("SFR", 200000)
##
##print "Land use:", myparcel.landuse
##mytax = myparcel.assessment()
##print mytax
#Modified Parcel Class
class Parcel: 
    numParcels = 0 #class variable created to count how many parcel objects have been created 
    def __init__(self, landuse, value, owner, parcelID): #initialize class
        self.landuse = landuse
        self.value = value
        self.owner = owner
        self.parcelID = parcelID
        Parcel.numParcels += 1 #count of parcels incremented by 1 whenever class initialized
    def assessment(self):
        if self.landuse == "Single Family value":
            rate = 0.05
        elif self.landuse == "Multiple Family value":
            rate = 0.04
        else:
            rate = 0.02
        assessment = self.value * rate
        return assessment
    def description(self):
        print self.owner, "is owner of parcel ID", self.parcelID, "(",self.numParcels,"entered), landuse type:",self.landuse,": $",self.value,", tax assessed: $",int(self.assessment()) 


##myparcel = Parcel("Single Family value", 250000, "Kwon", 23423)
##myparcel.description() #running this will print; no need to type print


parcel1 = Parcel("Single Family value", 250000, "Kwon", 23423)
parcel1.description()
parcel2 = Parcel("Multiple Family value", 505000, "Crye-Leike", 25013)
parcel2.description()
parcel3 = Parcel("Farm", 60000, "Harris", 10394)
parcel3.description()
