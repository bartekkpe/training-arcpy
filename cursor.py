#py 2.7
import arcpy

#add field to table/ shp
arcpy.AddField_management(fc_path, 'NewField', 'TEXT', field_length=50)

#read cursor
columns = ['Col1', 'Col2', 'Col3']
with arcpy.da.SearchCursor(fc_path, columns) as cursor:
    for row in cursor:
        print(row[0], row[2]) #print values of col 1 and 3

#update cursor
rows = arcpy.UpdateCursor(fc_path)
for row in rows:
    col2val = row.getValue('Col2')
    if row.getValue('Col1') < 7:
        row.setValue('Col3', col2val * 0.2)
        rows.updateRow(row)

del row
del rows

#get unique values of a column
my_col = set()
with arcpy.da.SearchCursor(fc_path, 'Col1') as cursor:
    for row in cursor:
        my_col.add(row)

del row
del rows
