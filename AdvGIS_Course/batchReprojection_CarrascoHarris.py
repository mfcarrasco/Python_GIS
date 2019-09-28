#Batch reprojection Tool
#Malle Carrasco-Harris 4/11/16

#Make a user-friendly tool to reproject raw datasets into target projection
#Left print script to be adapted later. 

import arcpy
from arcpy import env
env.overwriteOutput = True

try:
    #Input parameters
    env.workspace = inPath = arcpy.GetParameterAsText(0) #folder/gdb that is workspace
    target = arcpy.GetParameterAsText(1) #fc that has the desired spatial reference
    outFolder= arcpy.GetParameterAsText(2) #folder where either new file GDB or folder will be created

    if inPath.endswith(".gdb"):
        outGDB = arcpy.CreateFileGDB_management(outFolder, "Results") #new gdb that will hold output fc
    else:
        outFolder = arcpy.CreateFolder_management(outFolder, "Results") #new results folder that will hold output shapefiles

    inFC = arcpy.ListFeatureClasses() #feature classes in workspace 
    print "The Feature classes in this folder are ", inFC 

    targSpatial = arcpy.Describe(target).spatialReference.name #desired spatial reference.name object
    targSR = arcpy.Describe(target).spatialReference #desired spatial reference object
    print "The desired spatial reference is ", targSpatial

    listProjFC = [] #empty list to hold projected feature classes

    for fc in inFC: #for loop to go through all feature classes 
        inSpatial = arcpy.Describe(fc).spatialReference.name #spatial reference.name object for fcs in workspace
        print "The spatial reference for ", fc, " is ", inSpatial
        if inSpatial != targSpatial: #if statement to assess files that are not in the same spatial reference as target
            print fc, "does not have the same spatial reference."
            if fc.endswith(".shp"): #if statment to separate feature classes from shapefiles
                print "This is a shapefile"
                rootName = fc[:-4]
                print "The rootname for this shapefile is", rootName 
                outfc = str(outFolder) + r"/" + rootName + "_projected.shp"
                arcpy.Project_management(fc, outfc, targSR)
                print fc, "shapefile was just projected"
                arcpy.AddMessage(arcpy.GetMessages())
            else:
                print "This is a feature class"
                outfc = str(outGDB) +r"/"+ fc + "_projected" 
                print outfc
                arcpy.Project_management(fc, outfc, targSR)
                print fc, "was just projected"
                arcpy.AddMessage(arcpy.GetMessages())
            listProjFC.append(fc)
    print "The following feature classes were projected: "
    print listProjFC
    arcpy.AddMessage("The following feature classes were projected: {0}".format(listProjFC))

except: #report any error messages
  print arcpy.AddError("Could not complete the batch projection.")
  print arcpy.AddMessage(arcpy.GetMessages())