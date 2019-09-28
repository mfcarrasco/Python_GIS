#Assignment 10
#Malle Carrasco-Harris
#4/27/16

import arcpy
from arcpy import env
env.workspace = r"C:\GIS_Work\AdvGIS\PoliceData\PoliceData.gdb"
env.overwriteOutput = True

#Original feature classes
incidentsFC = "GraffitiIncidents"
patrolZonesFC = "PatrolZones"


#Create feature layers
arcpy.MakeFeatureLayer_management(incidentsFC, "incidents")
arcpy.MakeFeatureLayer_management(patrolZonesFC, "patrolZones")

try:
    with arcpy.da.SearchCursor("patrolZones", ("NAME",)) as cursor: #creating a search cursor to scroll through patrol zones.
        for row in cursor:
            print "The patrol zone name is",row[0] #checking that the search cursor is working. 
            zone = str(row[0])
            #Make a feature layer for each specific zone based on the zone row
            fieldName = "NAME"
            query = '"' + fieldName + '"=' + "'" +zone + "'" #zone query to narrow down the layer to just one zone
            arcpy.MakeFeatureLayer_management(patrolZonesFC, "selectedZoneLyr", query)
            print "A layer was successfully made for", row[0]
            #Select the incidents within the selected zone layer
            arcpy.SelectLayerByLocation_management("incidents", "WITHIN", "selectedZoneLyr")
            #Count the number of incidents within the zone
            number = int(arcpy.GetCount_management("incidents")[0])
            print "The number of incidents in ", zone," is ", number
            #Create an update cursor to enter the number of incidents into the attribute to the table, with the rows limited by the zone query
            with arcpy.da.UpdateCursor("patrolZones", ("INCIDENTS", "PRIORITY","SHAPE_Area"), query) as cursor:
                for row in cursor:
                    row[0] = number
                    #calculate density of incidents per square mile
                    incDensity = number/(row[2]/2589988.11) #need to convert from sq meters to sq miles
                    print "The incident density in this zone is ", incDensity, "graffiti incidents per square mile."
                    #priority assignment conditional statements
                    if incDensity >= 15:
                        row[1] = "TOP CONCERN"
                    elif incDensity >= 12:
                        row[1] = "HIGH CONCERN"
                    elif incDensity >= 6:
                        row[1] = "SOME CONCERN"
                    else:
                        row[1] = "LOW CONCERN"
                    print number, "incidents occured in this zone and the priority level is ", row[1],". This was successfully added to the attributes table."
                    cursor.updateRow(row)
except:
    print "Woops, an error occured:"
    print arcpy.GetMessages()
    