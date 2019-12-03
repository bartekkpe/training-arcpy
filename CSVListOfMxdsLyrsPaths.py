import os
import csv
import arcpy

pathToMxdsFolder = r'X:\\XX\\XX\\'
pathToCsvFile = r'X:\\XX\\XXX.csv'

with open(pathToCsvFile, 'wb') as csvFile:
    csvWriter = csv.writer(csvFile)
    for mainpath, directory, files in os.walk(pathToMxdsFolder):
        for f in files:
            if f.endswith('.mxd'):
                mxdPath = mainpath + f
                mxd = arcpy.mapping.MapDocument(mxdPath)
                for lyr in arcpy.mapping.ListLayers(mxd):
                    if lyr.supports("DATASOURCE"):
                        print(f, lyr.name, lyr.dataSource)
                        csvWriter.writerow([f, lyr.name, lyr.dataSource])
