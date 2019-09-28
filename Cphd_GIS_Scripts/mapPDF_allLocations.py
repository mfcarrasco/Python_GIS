#Make a map document from the last spot files and create a pdf to print
#need to use LastSpot.mxd

#CHANGE DATE to current date:
date = "14July"

import arcpy
from arcpy import env
#Set a workspace
workspace = r"C:\GIS_Work\Cphd_Locations"
env.workspace = workspace
env.overwriteOutput = True

#Call the pre-made map document (should be in Layout View)
mxd = arcpy.mapping.MapDocument(r"C:\GIS_Work\Cphd_Locations\LastSpot.mxd")
print "Called Map Document LastSpot.mxd"

#Create a layer out of the feature class created by the Overton Last Spot Script
locationsFC = r"C:\GIS_Work\Cphd_Locations\Locations.gdb\Overton_Locations"
locationsLyr = arcpy.MakeFeatureLayer_management(locationsFC, "Overton Locations") #Should add the layer to the map (and then must be saved if wanted for later)
print "Created a temporary layer using Overton Locations"

#Save the layer
arcpy.SaveToLayerFile_management(locationsLyr, "Overton_Locations.lyr")
print "Saved the overton park layer file"

#Add layer to map
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
addLayer = arcpy.mapping.Layer(r"C:\GIS_Work\Cphd_Locations\Overton_Locations.lyr")
arcpy.mapping.AddLayer(df, addLayer)
print "Added layer to map document"

#Create labels
layer = arcpy.mapping.ListLayers(mxd)[0]
layer.showLabels = True
print "Added labels. Be sure to check all appear in PDF"

#Save map document 
fileName = r"C:\GIS_Work\Cphd_Locations\LastSpot_"
mxd.saveACopy(fileName+date+".mxd") 
print "Saved the map document"

#Export PDF
map = arcpy.mapping.MapDocument(fileName+date+".mxd")
arcpy.mapping.ExportToPDF(map, fileName+date+".pdf")
print "PDF successfully exported" 

#Delete Overton Park Locations layer
arcpy.Delete_management(r"C:\GIS_Work\Cphd_Locations\Overton_Locations.lyr")
print "Deleted Overton Park Locations Layer file"
