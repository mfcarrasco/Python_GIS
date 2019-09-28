def areaCircle(radius): #define a function
    area = 3.141592 * radius ** 2
    return area
if __name__ == '__main__': #when executing the module within this script, then it will continue to test and print. This statement allows us to test the module from within the module, but will stop the rest of the script from running during an import. 
    print areaCircle(12) #to see result, add print in front of the function.
