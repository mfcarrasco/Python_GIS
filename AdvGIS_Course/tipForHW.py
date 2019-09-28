import arcpy
from arcpy import env

env.workspace = r"H:\6525\mfcrrsco\data\geoportal.gdb"

fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    desc = arcpy.Describe(fc)
    print fc, "Projection name is ",desc.spatialReference.name
    
##desc = arcpy.Describe(fc) #instantiates
##for item in desc.fields:
##    print item.name
##
##print desc.spatialReference.name
