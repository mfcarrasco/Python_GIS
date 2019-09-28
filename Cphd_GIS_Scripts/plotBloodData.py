#Plot Locational Data to show where snakes for which blood was collected.
#Ensure the file is called blood_ and that the sheet is named Data
#Goal: 1)From .xls, create a feature class
#2)project correctly



#Created by: Malle Carrasco-Harris

import arcpy
from arcpy import env
#Set a workspace
workspace = r"C:\GIS_Work\Cphd_Locations"
env.workspace = workspace
env.overwriteOutput = True


###1)Create a .gdb and import excel tabular data and create a feature class
###set gdb variables
##out_folder = workspace
##out_gdb = "Locations.gdb"
###Create File GDB
##arcpy.CreateFileGDB_management(out_folder, out_gdb)

##print out_gdb," was created."

out_gdb = "Locations.gdb"
#Set local variables:
in_table = "blood_samples_meeman.xls\Coordinates$"
x_coord = "LONG"
y_coord = "LAT"
out_layer = "location_GCS1984.lyr"
spat_ref = arcpy.SpatialReference(4326)#GCS_WGS_1984

#Make the XY event layer
arcpy.MakeXYEventLayer_management(in_table, x_coord, y_coord, out_layer, spat_ref)

print "Your layer ", out_layer," was created" #for debugging purposes

#Save to feature class
out_fc = "locationsFC_GCS1984"
arcpy.FeatureClassToFeatureClass_conversion(out_layer, out_gdb, out_fc)

print "Your feature class ", out_fc," was created" #for debugging purposes

#Update Workspace:
env.workspace =r"C:\GIS_Work\Cphd_Locations\Locations.gdb" 
#2) change projection from GCS to PCS
in_fc = out_fc
out_fc2 = "Blood_Locations_Meeman"
out_coord = arcpy.SpatialReference(3661) # "NAD_1983_NSRS2007_StatePlane_Tennessee_FIPS_4100"
transformation = "NAD_1983_NSRS2007_To_WGS_1984_1"

arcpy.Project_management(in_fc, out_fc2, out_coord, transformation)

print "Your projected feature class ",out_fc2," was created" #for debugging purposes

#Delete GCS fc to clean up .gdb

arcpy.Delete_management(out_fc)


