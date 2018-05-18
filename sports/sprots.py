# -*- coding: utf-8 -*-
import xlrd
import MySQLdb


book = xlrd.open_workbook("li.xls", "rb")
sheet = book.sheets()[0]

database = MySQLdb.connect(host="yb.upc.edu.cn", port=3306, user="yibantest", passwd="yibantest",
                           db="yibantest_integrate")
database.set_character_set('utf8')
cursor = database.cursor()
poj = sheet.cell(1, 0).value

print(sheet.cell(1, 0).value)

a = 1;
print(bool(0))
query = """INSERT INTO sports_user ( project, username,ranking,score, ord, out_record, record_info) VALUES (%s, %s, %s, %s, %s, %s, %s)"""

for r in range(4, sheet.nrows):
    ord = sheet.cell(r, 0).value
    ranking = sheet.cell(r, 0).value
    username = sheet.cell(r, 1).value
    score = sheet.cell(r, 2).value
    tmp = sheet.cell(r, 3).value
    record_info = sheet.cell(r, 4).value

    out_record = tmp=='1'and True or False

    values = (poj, username, ranking, score, ord, out_record, record_info)

    cursor.execute(query, values)

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

