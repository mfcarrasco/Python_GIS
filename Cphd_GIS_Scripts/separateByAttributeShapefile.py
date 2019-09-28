#Goal:Separate by attribute - want to separate individual snakes based on PIT ID
#created by Malle Carrasco-Harris
#Created: 4 August
#Most recent edit: 6 October
###Wanted to make this edition of the script to create individual shapefils in a folder for KDE in GME. 
##BE SURE TO CHANGE:
#NAME OF THE allID location to fit the file name
#Shapefolder they go into

import arcpy
from arcpy import env

#Set a workspace
env.workspace = r"C:\GIS_Work\Cphd_Locations"
env.overwriteOutput = True
#1) 
#Set Variables
out_gdb = "Locations.gdb"
allID = "C:\GIS_Work\Cphd_Locations\Locations.gdb\Meeman_Locations"

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
    arcpy.Select_analysis(allID, "C:\GIS_Work\Cphd_Locations\ID_Shapefiles_Meeman\Meeman_"+id+".shp", "ID"+'='+"'"+id+"'") #adjust shapefolder name and file prefix.

print "All the separate location by ID files have been created."

