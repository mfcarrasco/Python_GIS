#Goal:Separate by attribute - want to separate individual snakes based on PIT ID
#created by Malle Carrasco-Harris
#Created: 4 August
#Most recent edit: 4 August

import arcpy
from arcpy import env

#Set a workspace
env.workspace = r"C:\GIS_Work\Cphd_Locations"
env.overwriteOutput = True
#1) 
#Set Variables
out_gdb = "Locations.gdb"
allID = "C:\GIS_Work\Cphd_Locations\Locations.gdb\Overton_Locations"

fieldList = arcpy.ListFields(allID)
for field in fieldList:
    print field.name

#Input variable
idList = []
#Read the fc for different values in the ID field
with arcpy.da.SearchCursor(allID, "ID") as cursor:
    for row in cursor:
        if row[0] not in idList:
            idList.append(row[0])
print idList


#Use the ID list to select the points to create a new fc
for id in idList:
    arcpy.Select_analysis(allID, allID+"_"+id, "ID"+'='+"'"+id+"'")

print "All the separate location by ID files have been created."

