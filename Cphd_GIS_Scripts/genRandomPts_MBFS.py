#Generate Random Points
#Goal: Create random points in Meeman Biological Field Station


#Created by: Malle Carrasco-Harris
#3Feb2017

#Change date to current date
date = "16July2018"
import arcpy
from arcpy import env
#Set a workspace
workspace = r"C:\GIS_Work\Cphd_Locations\Locations.gdb"
env.workspace = workspace
env.overwriteOutput = True

#1)Generate Random Point in the feature of Meeman Biological Field Station
out_path =  workspace
out_name = "randomPts_"+date
con_feat = "C:\GIS_Work\Biology Boundaries\Biology_Boundary_NoPrcls.shp"
#Will automatically be generated as the same projection as Overton Park. 
arcpy.CreateRandomPoints_management(out_path, out_name, con_feat, "", 30)

print "Random points were successfully generated" 

#2) CHANGE PROJECTION TO WGS 1984 OR STEP 4 WON'T WORK
in_data = out_name
out_data = in_data+"_Project"
spat_ref = arcpy.SpatialReference(4326)
#trans_meth = "NAD_1983_NSRS2007_To_WGS_1984_1"

arcpy.Project_management(in_data, out_data, spat_ref) 

print "Projection successfully changed"

#3)Add XY coordinates to table.
in_feat = out_data

arcpy.AddXY_management(in_feat)

print "XY points were successfully generated"

#4) Convert Coordinates notation from Decimal degrees to decimal degree minutes
#DD_2 to DDM_2

#make table view

#arcpy.MakeTableView_management(in_feat, in_table)
in_table = in_feat
out_FC = "randomPts_"+date+"_DDM"
x_field = "POINT_X"
y_field = "POINT_Y"
out_coord = "DDM_2"
spat_ref = arcpy.SpatialReference(3661) #'NAD_1983_NSRS2007_StatePlane_Tennessee_FIPS_4100')


arcpy.ConvertCoordinateNotation_management(in_table, out_FC, x_field, y_field, "", out_coord, "", spat_ref)

print "Successfully converted coordinate notation"
                                           
                              
#Delete GCS fc to clean up .gdb

arcpy.Delete_management(in_table)
arcpy.Delete_management(out_name)

