#FIA dataset
#4/19
#Malle Carrasco-Harris
#finish code to produce max lat for all species 
import arcpy
from arcpy import env
env.workspace = r"H:\6525\mfcrrsco\Little"
env.overwriteOutput = True


fcList = arcpy.ListFeatureClasses()
lat = []
print fcList
for fc in fcList:#retrieve features y coordinate
    max = []
    with arcpy.da.SearchCursor(fc, ("SHAPE@Y",)) as cursor: #created search cursor onto fc. Created cursor on top of shape "token"
        for row in cursor:
            #to get only max latitude appeneded.
            max.append(row[0])
    lat.append(max)
print lat