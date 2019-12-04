import os
import arcpy

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
