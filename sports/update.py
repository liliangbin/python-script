# -*- coding: utf-8 -*-
import xlrd
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

book = xlrd.open_workbook("name.xls", "rb")
sheet = book.sheets()[0]

database = MySQLdb.connect(host="yb.upc.edu.cn", port=3306, user="yibantest", passwd="yibantest",
                           db="yibantest_integrate")
database.set_character_set('utf8')
cursor = database.cursor()
poj = sheet.cell(1, 0).value
record_info= "sdfsadf"
username = "关世伟"
print(sheet.cell(1, 0).value)
query = "UPDATE sports_user SET out_record = 1, record_info = '%s" % record_info + "' WHERE project = '%s" % poj + "' ,username = '%s" % username + "' "
cursor.execute(query)


for r in range(4, sheet.nrows):
    record_info = sheet.cell(r, 0).value
    username = sheet.cell(r, 1).value
    query = "UPDATE sports_user SET out_record = 1, record_info = '%s" % record_info + "' WHERE project = '%s" % poj + "' ,username = '%s" % username + "' "
    cursor.execute(query)

cursor.close()

database.commit()

database.close()

print ""
print "Done! "
print ""
columns = str(sheet.ncols)
rows = str(sheet.nrows)

print(columns)
print(rows)
