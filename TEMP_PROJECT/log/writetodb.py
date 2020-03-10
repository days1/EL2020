import sqlite3 as db
import sys

date = sys.argv[1]
temp = sys.argv[2]
humid = sys.argv[3]

conn = None

def create_temp_log(conn, log):
	sql = ''' INSERT INTO templogs(date_time, Temp, Humidity)
		VALUES(?,?,?);'''
	cur = conn.cursor()
	cur.execute(sql, log)
	conn.commit()
	print("Log inserted successfully into templogs table")
	return cur.lastrowid

try:
	conn = db.connect('templogs.db')
	print("Connected to database")
	log = (date, temp, humid)
	log_id = create_temp_log(conn, log)

except db.Error, e:
	print "Error %s:" %e.args[0]
	sys.exit(1)

finally:
	if conn:
		conn.close()
		print("Database connection closed")
