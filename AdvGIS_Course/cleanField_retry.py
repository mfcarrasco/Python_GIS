#Exam 2 - Question 2 - attempt to retry this script but it doesn't work
#Malle Carrasco-Harris
#3/31/16

import arcpy #import arcpy sitepackage
from arcpy import env

env.workspace = r"H:\6525\mfcrrsco\exam2\exam2.gdb" #defining the workspace
env.overwriteOutput = True
try:
    in_table = "cities"
    outFC = in_table + "_cleaned"
    #Save as new feature class 
    arcpy.CopyFeatures_management(in_table, outFC)
    #Createa  list of fields that are integer 
    intField = arcpy.ListFields(outFC, "", "Integer")
    #print intField #can be uncommented to use to check creation of list
    dropField = []
    for item in intField:
        print item.name
        dropField.append(item.name)
    
    arcpy.DeleteField_management(outFC, dropField)
    print "delete completed"

except:
    arcpy.GetMessages()