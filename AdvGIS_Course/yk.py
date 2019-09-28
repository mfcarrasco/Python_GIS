#Create fishnet and spatial join
import arcpy
from arcpy import env
env.workspace = r"C:\2016work\AdvancedGIS\LITTLE_ALL" #folder that contains all the .shp (Little's range maps) -change dir for use
env.overwriteOutput = True
fcList = arcpy.ListFeatureClasses()
print fcList #check

#define project - NAD1927 set by existing nad1927 shape file
desc = arcpy.Describe(r"C:\2016work\AdvancedGIS\join\nad1927.shp") #or coord = arcpy.SpatialReference(4267) 
coord = desc.spatialReference
for i in fcList:
    arcpy.DefineProjection_management(i,coord)
#two vectors that will hold spatial join results, join will overwrite outjoin later
join = r"C:\2016work\AdvancedGIS\join\fishnet20GCS.shp" #20km by 20km grid to cover study area (manually created) - change dir for use
outJoin = r"C:\2016work\AdvancedGIS\join\grid_out.shp" #spatial join output - change dir for use

for fc in fcList:
    drop = [] #to clean up fields in fc before spatial join
    print fc #check
    for i in arcpy.Describe(fc).fields:
        drop.append(i.name)
    print drop[2:]  #check
    arcpy.DeleteField_management(fc,drop[2:-1]) # [2:-1] because at least one column except FID, SHAPE need to be exist 
    arcpy.SpatialJoin_analysis(join,fc,outJoin) # spatial join
    arcpy.CopyFeatures_management(outJoin,join) #overwrite output to original grid.shp file
    arcpy.AddField_management(join,"a"+fc[:-7]) #add interpretable field name: -7 due to field name characters limit by 10
    arcpy.CalculateField_management(join,"a"+fc[:-7],"!Join_Count!","PYTHON") #calculate field equal to Join_Count
    arcpy.DeleteField_management(join,["Join_Count","TARGET_FID","CODE"]) #delete original Join_Count CODE etc. to clean up the table

#your output is a table in join (fishnet20GCS.shp)
