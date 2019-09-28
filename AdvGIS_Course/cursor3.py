import arcpy
from arcpy import env
env.workspace = r"H:\6525\mfcrrsco\census"
env.overwriteOutput = True

fc = "census_US.shp"
desc = arcpy.Describe(fc)
field = ("STATE_NAME","STATE_ABBR", "POP2000")
#hard coding: query = "\"STATE_NAME\" = 'Tennessee'" #Value has to have "" and the field name has to have ' ' So must use " " over entire query to create string. Use backslash \ to correct the usage of qutn marks. 

#soft coding
fieldName = "STATE_NAME"
value = 'Texas'
query = '"'+ fieldName + '"=' + "'" + value + "'"


with arcpy.da.SearchCursor(fc, field, query) as cursor:
    for row in cursor:
        print row[0], row[1], "Population 2000:", row[2]


