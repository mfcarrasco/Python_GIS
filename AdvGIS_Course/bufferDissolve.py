#Assignment 7 - 3/24
#In geoportal.gdb, buffer 5 km of all the point geometry shape type feature classes and save them to a new file geodatabase*.
#* you don't need to create a file geodatabase in the script but you know you can do it too! (just manually create filegeodatabse in your folder would be fine in this assignment)
#** challenge task: try output buffer option of dissolve type as "ALL".

import arcpy
from arcpy import env

env.workspace = (r"C:\GIS Work\AdvGIS\data\geoportal.gdb")
env.overwriteOutput = True

#Create output gdb
arcpy.CreateFileGDB_management(r"C:\GIS Work\AdvGIS\data", "buffer.gdb")

#choose if it's a POINT geometry shape
pointFC = arcpy.ListFeatureClasses("", "Point")
print pointFC

#Do a for loop for a list of point geometry shapes use arcpy.Buffer_analysis tool 
for fc in pointFC:
    output = r"C:\GIS Work\AdvGIS\data\buffer.gdb" 
    arcpy.Buffer_analysis(fc, output + "/buffer" +fc, "5 Kilometers", "", "", "ALL")