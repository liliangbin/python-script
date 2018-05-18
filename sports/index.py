# -*- coding: utf-8 -*-
import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

database = MySQLdb.connect(host="yb.upc.edu.cn", port=3306, user="yibantest", passwd="yibantest",
                           db="yibantest_integrate")

database.set_character_set("utf8")
cursor = database.cursor()
record_info = "dsfasdfasd"
proj = "男学生甲组100米(预赛)"
username = "关世伟"
query = "UPDATE  sports_user SET out_record = %s , record_info = %s  WHERE project = %s " % (
True, record_info, proj)
cursor.execute(query)
cursor.close()
database.commit()
database.close()

print ""
print "Done! "
print ""
