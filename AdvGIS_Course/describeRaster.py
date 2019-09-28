#In-class exercise: #2 - Describe a raster

import arcpy
from arcpy import env

env.workspace = r"H:\6525\mfcrrsco\TNraster"
env.overwriteOutput = True

##desc = arcpy.Describe("tnraster")
##
##print "Format: " + desc.format
##print "Dataset type: " + desc.dataType
##print "Compression type: " + desc.compressionType
##print "Band count: ", desc.bandCount
##print "Sensor Type: " + desc.sensorType
##print "Extent: ", desc.extent.XMin

desc = arcpy.Describe(r"H:\6525\mfcrrsco\shelby.shp")
clipExtent = desc.extent #create the extent to be used of the clip by describe object
arcpy.Clip_management("tnraster", str(clipExtent), "tnclip") #First parameter is the input raster, second is the STRING extent of the shelby shapefile to use as the clip parameters, third is the name of the output and it will go to the gdb of my workspace


