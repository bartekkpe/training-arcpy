# ArcMap py2.7

import arcpy

mxd = arcpy.mapping.MapDocument(r'C:\Project\Folder\File.mxd')
df = arcpy.mapping.ListDataFrames(mxd, 'My Data Frame')[0]

for lyr in arcpy.mapping.ListLayers(mxd, '*Sample Layer Name*', df):
  print(lyr.description)
  lyr.visible = True
  
mxd.save()

################
# ArcGIS py3.X #

import arcpy

aprx = arcpy.mp.ArcGISProject(r"C:\Projects\YosemiteNP\Yosemite.aprx")
m = aprx.listMaps("Yosemite National Park")[0]
for lyr in m.listLayers():
    if lyr.supports("DEFINITIONQUERY"):
        lyr.definitionQuery = ""
    if lyr.supports("SHOWLABELS"):
        lyr.showLabels = False
aprx.save()
del aprx
