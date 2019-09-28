#Plot Spatial Data to make a map for the locations of Overton snakes.
#Ensure the file is called Overton and that the sheet is named Coordinates
#Goals: 1)From .xls, create a feature class that is
#2)projected correctly
#3)Use as a user-friendly tool on ArcMap GUI. 

#Created by: Malle Carrasco-Harris
#Updated: 4 August

import arcpy
from arcpy import env
env.overwriteOutput = True

try:
    #Input parameters: 
    env.workspace = workspace = arcpy.GetParameterAsText(0) #Workspace folder
    #1)Create a .gdb and import excel tabular data and create a feature class
    #set gdb variables
    out_gdb = arcpy.GetParameterAsText(1) #the name of the new geodatabase including .gdb
    #Create File GDB 
    arcpy.CreateFileGDB_management(workspace, out_gdb)

    print out_gdb," was created."

    #Set local variables:
    in_table = arcpy.GetParameterAsText(2)#the spreadsheet, such as "Overton.xls\Coordinates$", where the tabular data is held
    x_coord = "Long"
    y_coord = "Lat"
    out_layer = "location_GCS1984.lyr"
    spat_ref = arcpy.SpatialReference(4326)#GCS_WGS_1984

    #Make the XY event layer
    arcpy.MakeXYEventLayer_management(in_table, x_coord, y_coord, out_layer, spat_ref)

    print "Your layer ", out_layer," was created" #for debugging purposes

    #Save to feature class
    out_fc = "locationsFC_GCS1984"
    out_gdb = arcpy.GetParameterAsText(1)
    arcpy.FeatureClassToFeatureClass_conversion(out_layer, out_gdb, out_fc)

    print "Your feature class ", out_fc," was created" #for debugging purposes

    #Update Workspace:
    env.workspace = workspace+"/"+out_gdb
    #must combine the two initial parameters r"C:\GIS_Work\Cphd_Locations\Locations.gdb" 
    #2) change projection from GCS to PCS
    in_fc = out_fc
    out_fc2 = arcpy.GetParameterAsText(3) #name of the new feature class to be created
    out_coord = arcpy.SpatialReference(3661) # "NAD_1983_NSRS2007_StatePlane_Tennessee_FIPS_4100"
    transformation = "NAD_1983_NSRS2007_To_WGS_1984_1"

    arcpy.Project_management(in_fc, out_fc2, out_coord, transformation)

    print "Your projected feature class ",out_fc2," was created" #for debugging purposes

    #Delete GCS fc to clean up .gdb

    arcpy.Delete_management(out_fc)

except: #report any error messages
  print arcpy.AddError("Could not complete Plot Overton Locations.")
  print arcpy.AddMessage(arcpy.GetMessages())

