#Plot Spatial Data to make a map for the locations of Overton snakes.
#Ensure the file is called Overton and that the sheet is named Coordinates
#Goal: 1)From .xls, create a feature class
#2)project correctly

#Update DATE value

#Created by: Malle Carrasco-Harris and updated 12 July 2017

import arcpy
from arcpy import env
#Set a workspace
workspace = r"C:\GIS_Work\Cphd_Locations"
env.workspace = workspace
env.overwriteOutput = True

date = "17July17"

###1)Create a .gdb and import excel tabular data and create a feature class
###set gdb variables
##out_folder = workspace
##out_gdb = "Locations.gdb"
###Create File GDB
##arcpy.CreateFileGDB_management(out_folder, out_gdb)
##
##print out_gdb," was created."

#Set local variables:
in_table = "Overton2015.xls\Coordinates$"
x_coord = "Long"
y_coord = "Lat"
out_layer = "location_GCS1984.lyr"
spat_ref = arcpy.SpatialReference(4326)#GCS_WGS_1984

#Make the XY event layer
arcpy.MakeXYEventLayer_management(in_table, x_coord, y_coord, out_layer, spat_ref)

print "Your layer ", out_layer," was created" #for debugging purposes

#Save to feature class
out_fc = "locationsFC_GCS1984"
out_gdb = "Locations.gdb"
arcpy.FeatureClassToFeatureClass_conversion(out_layer, out_gdb, out_fc)

print "Your feature class ", out_fc," was created" #for debugging purposes

#Update Workspace:
env.workspace =r"C:\GIS_Work\Cphd_Locations\Locations.gdb" 
#2) change projection from GCS to PCS
in_fc = out_fc
out_fc2 = "Overton_Locations_2015_"+date
out_coord = arcpy.SpatialReference(3661) # "NAD_1983_NSRS2007_StatePlane_Tennessee_FIPS_4100"
transformation = "NAD_1983_NSRS2007_To_WGS_1984_1"

arcpy.Project_management(in_fc, out_fc2, out_coord, transformation)

print "Your projected feature class ",out_fc2," was created" #for debugging purposes

#Delete GCS fc to clean up .gdb

arcpy.Delete_management(out_fc)



