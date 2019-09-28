#Creating a cursor object to access and manipulate tables in GIS - 2.
#Data Access module arcpy.da.SearchCursor
#4/12/16
import arcpy
from arcpy import env
env.workspace = r"H:\6525\mfcrrsco\census"
env.overwriteOutput = True

fc = "census_US.shp"

with arcpy.da.SearchCursor(fc, ("STATE_NAME","POP2000")) as cursor: #must close out tuple with comma
#created a cursor and will call it as cursor.
#with automatically exits out of edit session. No need to use del.
    for row in cursor: #row is dummy variable
        print row[0]," ", row[1] #0 is the state name and 1 is population; will iterate through all the rows
        