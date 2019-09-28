import arcpy #could also do from arcpy import _____ (define specific module)
arcpy.env.workspace = r"H:\6525\mfcrrsco\data\geoportal.gdb"  #arcpy is site package, env is class, workspace is env class attribute; the r is to take care of slashes
arcpy.env.overwriteOutput = True #these three lines should be routine when working with ArcGIS


outFolder = r"H:\6525\mfcrrsco\data\\" #put folder at the top of script so you can easily change it late if you prefer and then the rest of the script will be automatically updated if you change your outFolder variable; have to have the two backslashes.
clipFc = r"H:\6525\mfcrrsco\shelby.shp" #the clip feature is a variable so it can be changed easily

featureClasses = arcpy.ListFeatureClasses() #this will make it easier to select feature classes as a list index. Parantheses --> searching under our workspace.
print featureClasses

for fc in featureClasses:
    arcpy.Clip_analysis(fc, clipFc, outFolder + fc + "_clip.shp")