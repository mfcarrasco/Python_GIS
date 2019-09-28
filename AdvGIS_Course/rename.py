import os,arcpy
from os.path import basename
from arcpy import env
env.workspace = r"F:\Research\Little_range_maps\115New_download\\"

# set local variables
SPCD = "SPCD.txt"
desc = arcpy.Describe(SPCD)
field = "SPCD"
spcd_latin_name = []

os.chdir(r"F:\Research\Little_range_maps\115New_download\unzip_check\\")

with arcpy.da.SearchCursor(SPCD,("SPCD", "Genus", "Species")) as cursor:
    for column in cursor:
        for item in os.listdir(os.getcwd()):
            if basename(item)[:4] == column[1][:4].lower() and basename(item)[4:8] == column[2][:4].lower():
                os.rename(basename(item), str(column[0]) + basename(item))

 