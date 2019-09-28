#Creating a cursor object to access and manipulate tables in GIS - 1.
#4/12/16
import arcpy
from arcpy import env
env.workspace = r"H:\6525\mfcrrsco\census"
env.overwriteOutput = True

fc = "census_US.shp"

#first version of cursor arcpy.SearchCursor
rows = arcpy.SearchCursor(fc) #create variable for the cursor object (opens edit session)
row = rows.next() #the next object at the current index
#Create a rule
while row:
    print row.STATE_NAME, "population in 2000 was",row.POP2000#property for which field will be accessed
    row = rows.next() #acts to move cursor to next row (as a cursor)
#don't need to have "row" object when using for loop
for item in rows:
    print item.STATE_NAME

del rows #if use del, this safely closes an edit session (delete cursor object) 