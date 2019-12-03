import arcpy

mxd = arcpy.mapping.MapDocument(r'X:\\XX\\XXX.mxd')

df = arcpy.mapping.ListDataFrames(mxd, "New Data Frame")[0]
addLayer = arcpy.mapping.Layer(r"X:\\XX\\XXX.shp")
arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")
mxd.saveACopy(r"X:\\XX\\XXX.mxd")
del mxd, addLayer
