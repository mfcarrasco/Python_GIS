import arcpy
from arcpy import env
env.workspace = r"H:\6525\mfcrrsco\census"
env.overwriteOutput = True

fc = "census_US.shp"
fieldName = "STATE_NAME"
value = 'Tennessee'
query = '"'+ fieldName + '" = ' + "'" + value + "'"

#make feature layer

arcpy.MakeFeatureLayer_management(fc, "allStates" )#entire US as a feature layer; saved in memory not harddrive
arcpy.MakeFeatureLayer_management(fc, "TN", query) #selects only Tennessee as a select by attributes

#select by location
arcpy.SelectLayerByLocation_management("allStates", "BOUNDARY_TOUCHES", "TN") #allStates is now only those selected

#check output; be very comfortable with search cursor
with arcpy.da.SearchCursor("allStates", ("STATE_NAME",)) as cursor: #it's much faster because it looks up existing attributes table but doesn't make a new one in MakeFeatureLayer
    for row in cursor:
        print row[0]