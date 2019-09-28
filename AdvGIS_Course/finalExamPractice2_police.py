#Practicing the Police Data Assignment for final exam

import arcpy
from arcpy import env
env.workspace = r"C:\GIS_Work\AdvGIS\PoliceData_2\PoliceData.gdb"
env.overwriteOutput = True

#variable objects
zones = "PatrolZones"
incidents = "GraffitiIncidents"
zonesLyr = "ZonesLayer"
incidentsLyr = "IncidentsLayer"

#Make a Feature Layer for patrol zones and for incidents
arcpy.MakeFeatureLayer_management(zones, zonesLyr)
arcpy.MakeFeatureLayer_management(incidents, incidentsLyr)

with arcpy.da.SearchCursor(zonesLyr, ("NAME",)) as cursor:
    for row in cursor:
        print "The name of this patrol zone is ", row[0]
        zoneName = str(row[0])
        fieldName = "NAME"
        query = '"'+fieldName+ '"=' + "'"+ zoneName + "'"
        #Make a feature layer for each specific zone based on the row
        arcpy.MakeFeatureLayer_management(zones, "selectedZoneLyr", query)
        print "A Selection layer for ", row[0]," was created."
        #Select the incidents within the layer
        arcpy.SelectLayerByLocation_management(incidentsLyr, "WITHIN", "selectedZoneLyr")
        #Count the number of incidents within the layer
        count = int(arcpy.GetCount_management(incidentsLyr)[0])
        print "The number of incidents within ", row[0]," is ", count
        #Update the Incidents field with the count and update priority with rank:
        with arcpy.da.UpdateCursor(zonesLyr, ("INCIDENTS","PRIORITY", "SHAPE_Area"), query) as cursor:
            for row in cursor:
                row[0] = count #inserts the number of incidents in that layer
                density = count/(row[2]/2589988.11) #calculate incidents per square mile
                print "The incidents per square mile in this zone is ", density
                if density >= 15:
                    row[1] = "TOP CONCERN"
                elif density >=12:
                    row[1] = "HIGH CONCERN"
                elif density >= 6:
                    row[1] = "SOME CONCERN"
                else:
                    row[1] = "LOW CONCERN"
                print count, " incidents occured in this zone and the concern level is ", row[1]
                cursor.updateRow(row)

print "The attribute table has been updated to include incidents and priority"
                
        