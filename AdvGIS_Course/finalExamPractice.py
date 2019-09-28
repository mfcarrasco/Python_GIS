#Final exam practice

import arcpy
from arcpy import env
env.workspace = r"C:\GIS_Work\mfcrrsco\mfcrrsco\census"
env.overwriteOutput = True

featureClass = "census_US.shp"
##fieldList = arcpy.ListFields(featureClass)

##for field in fieldList:
##    print field.name

#Find the average population in the census dataset

##populationField = "POP2007"
##average = 0
##totalPop = 0
##recordsCounted = 0
##
##with arcpy.da.SearchCursor(featureClass, (populationField,)) as cursor:
##    for row in cursor: #don't forget this line! 
##        totalPop += row[0] #this number is in regards to the index position of the field name in the tuple. 
##
##average = totalPop/recordsCounted
##print "Average population for the United States in 2000 is " + str(average)

##query = '"POP2007" < 5010000'
##count = 0
##with arcpy.da.SearchCursor(featureClass, (populationField, "STATE_NAME"), query) as cursor:
##    for row in cursor:
##        print "The state ", row[1], "has a population of ", row[0]
##        count +=1
##        print count

#Selecting by location & Make a feature layer
#make feature layer for all states
#make a second layer of state of interest
#select layer by location to narrow down
#open a search cursor on all states (which has been narrowed down)

##state = "Texas"
##nameField = "STATE_NAME"
##
##
##
###arcpy.MakeFeatureLayer_management(featureClass, "AllStatesLayer")
##
###second layer of state of interest
##query = '"'+nameField+ '"=' + "'"+state+"'"
##arcpy.MakeFeatureLayer_management(featureClass, "SelectionStateLayerTX", query)
##
##arcpy.SelectLayerByLocation_management("AllStatesLayer", "BOUNDARY_TOUCHES", "SelectionStateLayerTX")
##with arcpy.da.SearchCursor("AllStatesLayer", (nameField,)) as cursor:
##    for row in cursor:
##        print row[0]

##arcpy.AddField_management(featureClass, "TEMP", "TEXT")
##
##fieldList = arcpy.ListFields(featureClass)
##for field in fieldList:
##    print field.name
    
##
##popField = "POP2000"
##stateField = "STATE_NAME"
##query1 = '"POP2000" > 5000000'

##with arcpy.da.UpdateCursor(featureClass, (popField, "TEMP", stateField), query1) as cursor:
##    for row in cursor:
##        row[1] = "MEGA"
##        cursor.updateRow(row)
        
##with arcpy.da.SearchCursor(featureClass, (stateField,"TEMP",)) as cursor:
##    for row in cursor:
##        if row[1] == "MEGA":
##            print row[0] + row[1]
#variables to create a new shapefile using these parameters of census US
##outpath = env.workspace
##desc = arcpy.Describe(featureClass)
##coord = desc.SpatialReference

###create a new shapefile
##outName = "insertPractice.shp"
##insertPractice = arcpy.CreateFeatureclass_management(outpath, outName, "POINT",spatial_reference = coord)
###add fields to the shapefile
##arcpy.AddField_management(insertPractice, "Describe", "TEXT")

###insert one row with those fields
##with arcpy.da.InsertCursor(insertPractice, ("SHAPE@XY", "Describe")) as cursor: #Kwon prefers fields to be hard coded
##    cursor.insertRow(((-89.45, 35.45),"First Point"))#multiple parantheses to make one argument
##                    
###practice inserting more than one row using loops
##fields = ("SHAPE@XY", "Describe")
##values = [((-89.60, 35.60), "Second Point"), ((-89.70, 35.70), "Third Point"), ((-89.80, 35.80), "Fourth Point")]
##with arcpy.da.InsertCursor(insertPractice, fields) as cursor:
##    for row in values:
##        cursor.insertRow(row)

 