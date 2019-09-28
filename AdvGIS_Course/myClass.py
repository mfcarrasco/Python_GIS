##class MyClass: #start with uppercase first when creating a class (that way others know this is a class)
##    var = "this is var inside class"
##    def func(self,radius):
##        print "This is a message inside"
##        area = 3.14 * radius**2
##        return area
##
##
##print MyClass.func(3)

class Employee: #construction of class is called instance; class is the container that can handle interrelated variables and functions. 
    empCount = 0 #class variable
    def __init__(self, name, salary): #initializing specialied function __init__; constructs the variables self, name, salary. Self is the function itself.
        self.name = name #has property that you create and will be a name you supply (will really be Employee.name because self is Employee)
        self.salary = salary #has object propery that is added by your parameter
        Employee.empCount +=1 #incremented by 1 whenever you initilize it. 

    def displayCount(self): #method name
        print "Total Employee is", Employee.empCount
    def displayEmployee(self):
        print "Name: ", self.name, "Salary: ", self.salary

emp1 = Employee("Harris", 1000) #name, salary (don't provide anything for self); no longer just a variable but an object that has been "instanciazed". properties: function and method
#When you instaniate it will be assigned to the name you give it; that's why the self is called "self": it assigns the function to the variable (object) name you give it.
#Class gets insansiated to your emp; it can be instantiated to however many objects you choose. 
emp1.displayCount()
emp1.displayEmployee()

emp2 = Employee("Kwon", 200)
emp3 = Employee("Sarah", 300)
emp4 = Employee("Andrew", 20)

emp2.displayEmployee()
emp2.displayCount()
