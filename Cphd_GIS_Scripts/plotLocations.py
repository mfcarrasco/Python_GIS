#Plot Locational Data
#Goal: 1)From .xls, create a feature class
#2)project correctly
#3)separate by attribute
#4)group as layer package

#Created by: Malle Carrasco-Harris
#12May

import arcpy
from arcpy import env
#Set a workspace
workspace = r"C:\GIS_Work\SpatialDataAnalysis_12May"
env.workspace = workspace
env.overwriteOutput = True


#1)Create a .gdb and import excel tabular data and create a feature class
#set gdb variables
out_folder = workspace
out_gdb = "SDA_12May.gdb"
#Create File GDB
arcpy.CreateFileGDB_management(out_folder, out_gdb)

print out_gdb," was created."

#Set local variables:
in_table = "OP_Location12May.xls\coordinates$"
x_coord = "Long"
y_coord = "Lat"
out_layer = "location_GCS1984.lyr"
spat_ref = arcpy.SpatialReference(4326)#GCS_WGS_1984

#Make the XY event layer
arcpy.MakeXYEventLayer_management(in_table, x_coord, y_coord, out_layer, spat_ref)

print "Your layer ", out_layer," was created" #for debugging purposes

#Save to feature class
out_fc = "locationsFC_GCS1984"
arcpy.FeatureClassToFeatureClass_conversion(out_layer, out_gdb, out_fc)

print "Your feature class ", out_fc," was created" #for debugging purposes


env.workspace =r"C:\GIS_Work\SpatialDataAnalysis_12May\SDA_12May.gdb" 
#2) change projection from GCS to PCS
in_fc = out_fc
out_fc2 = "locations_12May"
out_coord = arcpy.SpatialReference(3661) # "NAD_1983_NSRS2007_StatePlane_Tennessee_FIPS_4100"
transformation = "NAD_1983_NSRS2007_To_WGS_1984_1"

arcpy.Project_management(in_fc, out_fc2, out_coord, transformation)

print "Your projected feature class ",out_fc2," was created" #for debugging purposes

#Delete GCS fc to clean up .gdb

arcpy.Delete_management(out_fc)

#3) Separate by ID
#Started 18May

##fieldList = arcpy.ListFields(out_fc2)
##for field in fieldList:
##    print field.name

#Input variable
allIDfc = out_fc2
idList = []
#Read the fc for different values in the ID field
with arcpy.da.SearchCursor(allIDfc, "ID") as cursor:
    for row in cursor:
       if row[0] not in idList:
           idList.append(row[0])

print idList

#Using the ID list to select the points to create a new fc
for id in idList:
   arcpy.Select_analysis(allIDfc, out_fc2+"_"+id, "ID"+'='+"'"+id+"'")

print "All the separate location files have been created."

#Export to PDF (need to create a map doc)