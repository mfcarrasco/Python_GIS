import os, arcpy, zipfile
from zipfile import ZipFile
from arcpy import env
env.workspace = r"F:\Research\Little_range_maps\115New_download\zip_check\\"

env.overwriteOutput = True

os.chdir(r"F:\Research\Little_range_maps\115New_download\zip_check\\")
outFolder = r"F:\Research\Little_range_maps\115New_download\unzip_check\\"

for item in os.listdir(os.getcwd()):
    if item.endswith(".zip"):
        zip_file = ZipFile(item,"r")
        for name in zip_file.namelist():
            zip_file.extract(name,outFolder)
            #zip_file.close()