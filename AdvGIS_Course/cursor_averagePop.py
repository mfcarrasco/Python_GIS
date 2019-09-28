#calculating average population
#add up population and then divide by the total number of states
import arcpy
from arcpy import env
env.workspace = r"H:\6525\mfcrrsco\census"
env.overwriteOutput = True

fieldName = ("STATE_NAME", "POP2007") #soft coded tuple for name
fc = "census_US.shp"


totalPOP= 0
recordsCount = 0
with arcpy.da.SearchCursor(fc, fieldName) as cursor:
    for row in cursor:
        totalPOP += row[1]
        recordsCount +=1

average = totalPOP/ recordsCount
print "The average population per state in the US is " + str(average)

        