#Update cursor
import arcpy
from arcpy import env
env.workspace = r"H:\6525\mfcrrsco\census"
env.overwriteOutput = True

fc = "census_US.shp"
arcpy.AddField_management(fc, "TEMP", "TEXT")





field = ("STATE_NAME","STATE_ABBR", "POP2000", "TEMP")

#variables for query
fieldName = "STATE_NAME"
value = 'Texas'

#query = '"'+ fieldName + '"=' + "'" + value + "'"
query1 = '"POP2000" > 5000000'

with arcpy.da.UpdateCursor(fc, field, query1) as cursor:
    for row in cursor:
        row[3] = "MEGA"
        cursor.updateRow(row) #update row is a method that will be done for every row
        

