# -*- coding: utf-8 -*-

import xlrd

import MySQLdb

import datetime

xlsfile = r'li.xlsx'

book = xlrd.open_workbook(xlsfile)

# 获取sheet的数量

count = len(book.sheets())
sheet = book.sheets()[0]

# 设置连接数据库

database = MySQLdb.connect(host="yb.upc.edu.cn", port=3306, user="yibantest", passwd="yibantest",
                           db="yibantest_integrate")
# 设置字符集

database.set_character_set('utf8')

cursor = database.cursor()

cursor.execute('SET NAMES utf8;')

cursor.execute('SET CHARACTER SET utf8;')

cursor.execute('SET character_set_connection=utf8;')

starttime = datetime.datetime.now()

print '开始时间：%s' % (starttime)

# 循环sheet

query = """INSERT INTO instructor_evaluate_student ( number, name, sex, password,nation , birthday ,college, grade,major,school_class,hometown, instructor_name,second_instructor) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s)"""

for r in range(1, sheet.nrows):
    number = sheet.cell(r, 1).value
    name = sheet.cell(r, 2).value
    sex = sheet.cell(r, 3).value
    password = sheet.cell(r, 4).value
    nation = sheet.cell(r, 5).value
    birthday = sheet.cell(r, 6).value
    college = sheet.cell(r, 7).value
    grade = sheet.cell(r, 8).value
    major = sheet.cell(r, 9).value
    school_class = sheet.cell(r, 10).value
    hometown = sheet.cell(r, 11).value
    instructor_name = sheet.cell(r, 12).value
    second_instructor = sheet.cell(r, 13).value
    values = (
        number, name, sex, password, nation, birthday, college, grade, major, school_class, hometown,
        instructor_name,
        second_instructor)

    cursor.execute(query, values)

cursor.close()

database.commit()

database.close()

endtime = datetime.datetime.now()

print (endtime)

print (endtime - starttime)
