import os
import arcpy

'''Turn on Layout View in ArcGIS and save mxd file'''

######################
##### SINGLE MAP #####
######################

###### ----- Export Specific mxd ----- #####

pathToMXDFile = r'C:\\MXDs\\File.mxd'
pathToPDFExportFile = r'C:\\Export\\File.pdf'
mxd = arcpy.mapping.MapDocument(pathToMXDFile)
arcpy.mapping.ExportToPDF(mxd, pathToPDFExportFile)

##### ----- Export Specific mxds ----- #####

pathToMXDsFolder = r'C:\\MXDs\\'
listOfMXDs = ['File1.mxd', 'File2.mxd']
pathToPDFs = r'C:\\Export\\'

for mxd in listOfMXDs:
    thisMxd = arcpy.mapping.MapDocument(os.path.join(pathToMXDsFolder, mxd))
    thisPdf = mxd[:-4] + '.pdf'
    arcpy.mapping.ExportToPDF(thisMxd, os.path.join(pathToPDFs, thisPdf))

##### ----- Export All mxds ----- #####

pathToMXDsFolder = arcpy.env.workspace = r'C:\\MXDs\\'
pathToPDFs = r'C:\\Export\\'

mxd_list = arcpy.ListFiles('*.mxd')
for mxd in mxd_list:
    thisMxd = arcpy.mapping.MapDocument(os.path.join(pathToMXDsFolder, mxd))
    thisPdf = mxd[:-4] + '.pdf'
    arcpy.mapping.ExportToPDF(thisMxd, os.path.join(pathToPDFs, thisPdf))

#############################
##### DATA DRIVEN PAGES #####
#############################

##### ----- Export Specific mxd Data Driven Pages ----- #####

pathToMXDFile = r'C:\\MXDs\\File.mxd'
pathToPDFExportFile = r'C:\\Export\\File.pdf'
mxd = arcpy.mapping.MapDocument(pathToMXDFile)
ddp = mxd.dataDrivenPages
ddp.exportToPDF(pathToPDFExportFile, resolution=int("300"), image_quality="BEST", colorspace="RGB", picture_symbol="VECTORIZE_BITMAP", layers_attributes="NONE")

##### ----- Export Specific mxds Data Driven Pages ----- #####

pathToMXDsFolder = r'C:\\MXDs\\'
listOfMXDs = ['File1.mxd', 'File2.mxd']
pathToPDFs = r'C:\\Export\\'

for mxd in listOfMXDs:
    thisMxd = arcpy.mapping.MapDocument(os.path.join(pathToMXDsFolder, mxd))
    thisPdf = mxd[:-4] + '.pdf'
    ddp = thisMxd.dataDrivenPages
    ddp.exportToPDF(os.path.join(pathToPDFs, thisPdf), resolution=int("300"), image_quality="BEST", colorspace="RGB", picture_symbol="VECTORIZE_BITMAP", layers_attributes="NONE")

##### ----- Export All mxds Data Driven Pages ----- #####

pathToMXDsFolder = arcpy.env.workspace = r'C:\\MXDs\\'
pathToPDFs = r'C:\\Export\\'

mxd_list = arcpy.ListFiles('*.mxd')
for mxd in mxd_list:
    thisMxd = arcpy.mapping.MapDocument(os.path.join(pathToMXDsFolder, mxd))
    thisPdf = mxd[:-4] + '.pdf'
    ddp = thisMxd.dataDrivenPages
    ddp.exportToPDF(os.path.join(pathToPDFs, thisPdf), resolution=int("300"), image_quality="BEST", colorspace="RGB", picture_symbol="VECTORIZE_BITMAP", layers_attributes="NONE")
