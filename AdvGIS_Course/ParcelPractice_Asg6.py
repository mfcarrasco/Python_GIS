#Parcel practice

class Parcel: #this is the class; must use class keyword
    numParcel = 0
    def __init__(self, landuse, value, owner, ID): #__init__ is method; __init__ initializes objects so they can be used.
        self.landuse = landuse
        self.value = value
        self.owner = owner
        self.ID = ID
        Parcel.numParcel += 1 
    def assessment(self):
        if self.landuse == "SFR":
            rate = 0.05
        elif self.landuse == "MFR":
            rate = 0.04
        else:
            rate = 0.02
        assessment = self.value * rate
        return assessment
    def description(self):
        print self.owner,"is owner of parcel ID of ", self.ID,"(",self.numParcel,"parcels entered)\nlanduse type: ",self.landuse," : " ,self.value, "tax assessed: $", self.assessment()
        
if "__name__" == "__main__":
    parcel1 = Parcel("SFR", 50000, "Malle", "6793")
    parcel1.description()
    parcel2 = Parcel("MFR", 45000, "Jeremy", 12345)
    parcel2.description()
    parcel3 = Parcel("truck", 123000, "James", 8904)
    parcel3.description()



