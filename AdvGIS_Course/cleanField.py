#Exam 2 - Question 2
#Malle Carrasco-Harris
#3/31/16

import arcpy #import arcpy sitepackage
from arcpy import env

env.workspace = r"H:\6525\mfcrrsco\exam2\exam2.gdb" #defining the workspace
env.overwriteOutput = True
try:
    in_table = r"H:\6525\mfcrrsco\exam2\exam2.gdb\cities"
    outFC = in_table + "_cleaned"
    #Save as new feature class 
    arcpy.CopyFeatures_management(in_table, outFC)
    #Createa  list of fields that are integer 
    intField = arcpy.ListFields(in_table, "", "Integer")
    #print intField #can be uncommented to use to check creation of list

    #Create a for loop that will delete all fields whose field type is Integer
    for field in intField:
        outFC = r"H:\6525\mfcrrsco\exam2\exam2.gdb\cities_cleaned"
        arcpy.DeleteField_management(outFC, field)
        print "delete completed"

except:
    arcpy.GetMessages()