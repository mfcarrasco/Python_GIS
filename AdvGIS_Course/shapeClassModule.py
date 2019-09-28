#class should calculate parameters area, description of shape (square like, vertically tall, horizontally long) 
#Arguments WIDTH x and HEIGHT y

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "Shape not known yet"
        self.author = "Author not known yet"
    def area(self): #(since this is a method, we don't have to provide anything becuase it's already initialized)
        return self.x * self.y
    def perimeter(self):
        return self.x * 2 + self.y * 2
    def describe(self, text):
        self.description = text
    def author(self, text):
        self.author = text
    def scale(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale