#Goal:Separate by attribute - want to separate individual snakes based on PIT ID
#created by Malle Carrasco-Harris
#Created: 4 August
#Most recent edit: 4 August

import arcpy
from arcpy import env
try:
    env.overwriteOutput = True
    #1) 
    #Set Variables
    env.workspace = out_gdb = arcpy.GetParameterAsText(0) #geodatabase within workspace
    allID = arcpy.GetParameterAsText(1) #feature class within geodatabase

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

except: #report any error messages
  print arcpy.AddError("Could not complete separate by attribute.")
  print arcpy.AddMessage(arcpy.GetMessages())