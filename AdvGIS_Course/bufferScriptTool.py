import arcpy
from arcpy import env

env.workspace = r"C:\GIS Work\AdvGIS\data\geoportal.gdb"
env.overwriteOutput = True

fc = "Fire"
outFC = "Fire_buffer"
distance = "2 Kilometers"

arcpy.Buffer_analysis(fc, outFC, distance)