#Clip geoprocessing exercise
#Malle Carrasco-Harris
#3/29/16

#Import arcpy module and set environment variables

import arcpy
from arcpy import env
try:
    env.workspace = r"H:\6525\mfcrrsco\data\Lesson1"
    env.overwriteOutput = True
    
    #Set variables and output folder directory
    outFolder = r"H:\6525\mfcrrsco\data\Lesson1\clip.gdb" #output is going to be a FEATURE CLASS so need to be saved in .gdb (this gdb is not exam)
    clipFC = "TNoutline.shp" #have to put shp becuase it is not a feature class, which are saved under a file geodatabase. Shapeclasses are not saved under .gdb
# List the feature classes in my folder
    fcList = arcpy.ListFeatureClasses("us_*")
#Loop through feature classes that start with us_ and clip to TN boundary
    
    for fc in fcList:
        arcpy.Clip_analysis(fc, clipFC, outfolder+ fc + "__TNclip.shp")

except:
    print "There's an error"
    arcpy.GetMessages()

#shapefile is same as fc but data structure is different. Shapefile is stand alone file; feature classes belong in .gdb

