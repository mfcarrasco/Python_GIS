#In-class exercise: #2 - Describe a raster

##import arcpy
##from arcpy import env
##
##env.workspace = r"H:\6525\mfcrrsco\TNraster"
##env.overwriteOutput = True
##
##desc = arcpy.Describe(r"H:\6525\mfcrrsco\shelby.shp") #describing the clip file so I can use it's extent
##clipExtent = desc.extent #create the extent to be used of the clip by describe object
##try:
##arcpy.Clip_management("tnraster", str(clipExtent), "tnclip")
###First parameter is the input raster,
###second is the STRING extent of the shelby shapefile to use as the clip parameters,
###third is the name of the output and it will go to the gdb of my workspace
##except:
##    print "There is an error"
##    print arcpy.GetMessages()#if we don't put any number, will return any message


#Making an error
import arcpy
from arcpy import env

env.workspace = r"H:\6525\mfcrrsco\TNraster"
env.overwriteOutput = True

desc = arcpy.Describe(r"H:\6525\mfcrrsco\shelby.shp") #describing the clip file so I can use it's extent
clipExtent = desc.extent #create the extent to be used of the clip by describe object
try:
    arcpy.Clip_management("error_raster", str(clipExtent), "tnclip")
#First parameter is the input raster,
#second is the STRING extent of the shelby shapefile to use as the clip parameters,
#third is the name of the output and it will go to the gdb of my workspace
except:
    print "There is an error"
    print arcpy.GetMessages()#if we don't put any number, will return any message