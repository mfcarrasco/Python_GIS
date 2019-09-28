#Kwon doing cleanField as covering exam 2
#4/4/16

import arcpy #import arcpy sitepackage
from arcpy import env

#set up workspace
env.workspace = r"H:\6525\mfcrrsco\exam2\exam2.gdb"
env.overwriteOutput = True

desc = arcpy.Describe("cities")
fields = desc.fields #will create field data object - property of interest is type and name

#copy features
arcpy.CopyFeatures_management("cities", "cities_copy")

dropField = [] #empty list where we will add integer types
for field in fields:
    #print field.name, "is field type of, ", field.type
    if field.type == "Integer":
        dropField.append(field.name)

print dropField

arcpy.DeleteField_management("cities_copy", dropField)
