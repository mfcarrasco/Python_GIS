#Export multiple attribute tables to single csv
#Python code from Mov Eco Tools
#Export all of the attribute information from multiple feature classes stored in the input file
#gdb toa  single CSV file.
#Assumption: all of the FCs in the 'input DB' database share the same schema.
#Edit the 'inputDB' and 'outpath' path variables as necessary


#Created 12 July 2017

#User defined parameters

inputDB = r"C:\GIS_Work\Cphd_Locations\AttributesToCSV.gdb"
outputpath = r"C:\GIS_Work\Cphd_Locations\AttributeInfo.csv"


#Script parameters
import arcpy, string
arcpy.env.workspace = inputDB
csvoutput = []
count = 0

#Function definition to get the non-spatial field names from a feature class
def get_fieldnames(fields):
    fields_array = []
    for field in fields:
        if field.type !="Geometry":
            fields_array.append(field.name)
    return fields_array

#Iterate through each feature class in the chosen database and write out hte non-spatial attribute fields

print "Starting operation..."
for fc in arcpy.ListFeatureClasses():
    print fc
    fields = arcpy.ListFields(fc)
    fieldnames = get_fieldnames(fields)
    if count == 0:
        csvoutput.append(",".join(fieldnames))
    rows = arcpy.SearchCursor(fc)
    for row in rows:
        outputrow = []
        for fieldname in fieldnames:
            outputrow.append(str(row.getValue(fieldname)))
        outputrow = ",".join(outputrow)
        csvoutput.append(outputrow)
    del fields
del rows

count = count+1

#Open the output file (create if it doesn't exist) and write attribute info
f = open(outputpath, 'w')
f.write('\n'.join(csvoutput))
f.close()

print "Finished writing " + str(count) + " rows to csv file."


