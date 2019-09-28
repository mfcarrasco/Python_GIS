#Exam 2 - Question 1
#Malle Carrasco-Harris
#3/31/16

class Circle: #Class variable created to calculate area and circumference of a circle of a specified radius. 
    def __init__(self, radius): #initialize class; user provides radius of circle.
        self.radius = radius #instantiate class
    def area(self): #area method
        area = 3.14 * radius**2
        return area
    def circumference(self): #circumference method
        circumference = 2 *3.14 * radius
        return circumference
    def description(self):
        print "With a radius of ", self.radius," a circle has an area of: ", int(self.area," and circumference of: ", int(self.circumference()),"."

#shape1 = Circle(5)
Circle.area(5)                                                                          
#circle1.description()