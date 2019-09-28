#This script uses map algebra to find values in an elevation raster greater than 100 meters
#4/4/16

import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = r"H:\6525\mfcrrsco\data1\USA.gdb"
env.overwriteOutput = True

#Specify the input raster
inRaster = "foxlake"
cutoffElevation = 3100

#Check out the Spatial Analyst extension; allows you to use Spatial analyst extention (in arcmap we do this through customize > extensions)
arcpy.CheckOutExtension("Spatial")

#Make a map algebra expression and save the resulting raster; Raster is a function from spatial analyst; will select the cutOffElevation value
outRaster = Raster(inRaster) > cutoffElevation
outRaster.save("foxlake3100") #Raster object method "save" to save the file



