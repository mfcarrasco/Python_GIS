import arcpy #site package
#or from arcpy import certain module
from arcpy import env #can do this to only a certian module from the package; also allows you to omit arcpy.

env.workspace = r"H:\6525\mfcrrsco\data\geoportal.gdb" 
env.overwriteOutput = True

desc = arcpy.Describe("School") #since it returns an object, we can assign it to a variable

print "Shape Type: " + desc.shapeType
print "Feature Type: " + desc.featureType
print "Extent: " + str(desc.extent.XMin)
print "Extent: ", desc.extent.XMin #same as above, but without string



