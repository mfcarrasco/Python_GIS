#FIA dataset
#4/19
#Malle Carrasco-Harris

import arcpy
from arcpy import env
env.workspace = r"H:\6525\mfcrrsco\Little"
env.overwriteOutput = True

fc = "375betupapy.shp"

desc = arcpy.Describe(fc)

for i in desc.fields:#calling up the fields in the attribute tables by name
    print i.name
    
#retrieve the centroid x & y coordinates
xy = []
with arcpy.da.SearchCursor(fc, ("SHAPE@XY",)) as cursor: #created search cursor onto fc. Created cursor on top of shape "token"
    for row in cursor:
        xy.append(row[0])

print len(xy)

#retrieve the second elementy in the row (the y)
with arcpy.da.SearchCursor(fc, ("SHAPE@XY",)) as cursor: #created search cursor onto fc. Created cursor on top of shape "token"
    for row in cursor:
        print row[0][1] #accessing the second item in a nested item (accessing the second item in the tuple x&y

#retrieve features y coordinate
lat = []
with arcpy.da.SearchCursor(fc, ("SHAPE@Y",)) as cursor: #created search cursor onto fc. Created cursor on top of shape "token"
    for row in cursor:
        lat.append(row[0])

print max(lat)