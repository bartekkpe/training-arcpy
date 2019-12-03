import arcpy, os

mxdPath = r'X:\\XX\\XXX.mxd'
outPath = r'X:\\XX\\'

mxd = arcpy.mapping.MapDocument(mxdPath)
layers = arcpy.mapping.ListLayers(mxd)
for lyr in layers:
    exportLyr = os.path.join(outPath, str(lyr.name) + '.lyr')
    lyr.saveACopy(exportLyr)
