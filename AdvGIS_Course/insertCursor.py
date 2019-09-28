#insert cursor

import arcpy
from arcpy import env
env.workspace = r"H:\6525\mfcrrsco\census"
env.overwriteOutput = True

outPath = env.workspace
desc = arcpy.Describe("census_US.shp")
coord = desc.SpatialReference

#arcpy.CreateFeatureclass_management(outPath, "fieldWork.shp", "POINT",spatial_reference = coord)

arcpy.AddField_management("fieldWork.shp", "DESCRIB", "TEXT")

field = ("SHAPE@XY", "DESCRIB")
with arcpy.da.InsertCursor("fieldWork.shp", field) as cursor:
    cursor.insertRow(((-90.43, 35.43), "first")) #multiple parantheses becuase insertRow only takes single argument
    
    