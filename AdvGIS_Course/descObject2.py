import arcpy #site package
#or from arcpy import certain module
from arcpy import env #can do this to only a certian module from the package; also allows you to omit arcpy.

env.workspace = r"H:\6525\mfcrrsco\data\geoportal.gdb" 
env.overwriteOutput = True
work = env.workspace


descFc = arcpy.Describe(work)
workItems = descFc.children #workItems will have all the underlying describe object(instead of having to do a for loop)
for item in workItems:
    print item.name + " shape type is: " + item.shapeType