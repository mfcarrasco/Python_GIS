import shapeClassModule

rectangle = shapeClassModule.Shape(100, 130) #remember we import modules and then run them using module.function
print rectangle.area()
print rectangle.perimeter()
print rectangle.description
rectangle.describe("The shape is a rectangle ")
print rectangle.description#parameters are updated accordingly
rectangle.scale(10)
print rectangle.area()#parameters are updated accordingly becuase things are interrelated in a class.
print rectangle.perimeter()