import arcpy

filename = 'C:/Project/folder/data.shp'
field = 'my_field'

with arcpy.da.UpdateCursor(filename, field) as cursor:
    for index, row in enumerate(cursor, 1):
        row[0] = 'sample text' + str(index)
        cursor.updateRow(row)
