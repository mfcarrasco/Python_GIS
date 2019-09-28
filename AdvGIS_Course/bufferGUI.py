#Creating GUI tools - Buffer
#Malle Carrasco-Harris
#4/7/16

import arcpy
from arcpy import env

env.workspaceOutput = r"H:\6525\mfcrrsco\data\geoportal.gdb"
env.overwriteOutput = True

#Variable settings
#arcpy.GetParameterAsText(0) #allows users to enter what they want
try:
    fc = arcpy.GetParameterAsText(0) #index of 0 is will be the first parameter asked
    outFc = arcpy.GetParameterAsText(1)
    distance = arcpy.GetParameterAsText(2)
    #geoprocessing
    arcpy.Buffer_analysis(fc, outFc, distance, dissolve_option = "ALL")
    arcpy.AddMessage("Task completed") #printed out to GUI but not interactive window
except:
    arcpy.AddError("There's an error") #adds errors to the heirachical order
    arcpy.AddMessage(arcpy.GetMessages())
