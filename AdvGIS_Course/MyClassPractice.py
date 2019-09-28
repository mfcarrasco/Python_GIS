class Myclass:
    var = "This is class variable"
    def __init__(self, name):# first parameter always self in a class
        self.name = name
    def funct(self):#using method and a function within aclass so ALWAYS start with self
        print "This is method print", self.name
        
foo = Myclass("Malle") #this step is called instantiate. This instance of class assigned to foo. now foo become object
print foo.var # no parantheses because it is not an attribute and it is not a method so NO parantheses

foo.funct() #need to put parantheses becuase funct is a method; foo is the "self" becuase it has the instance of the class

foo1 = Myclass("sara")
foo2 = Myclass("bob")
foo3 = Myclass ("jeff")