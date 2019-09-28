#Exam 2 - Question 1
#Malle Carrasco-Harris
#3/31/16

class Circle: #Class variable created to calculate area and circumference of a circle of a specified radius. 
    def __init__(self, radius): #initialize class; user provides radius of circle.
        self.radius = radius
    def area(self): #area method
        area = 3.14 * (self.radius)**2
        return area
    def circumference(self): #circumference method
        circumference = 2 *3.14 * self.radius
        return circumference
    def description(self): #description method
        print "A circle with a radius of ", self.radius," has an area of: ", float(self.area())," and circumference of: ", float(self.circumference()),"." #description method provides statement with decimal results

if __name__ == "__main__":#Test codes when runnign script directly; will not run test codes when run as module outside of script
    circle1 = Circle(3)
    circle1.description()
    circle2 = Circle(10)
    circle2.description()
    circle3 = Circle(45)
    circle3.description()