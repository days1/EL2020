# This script uses the parameters 'date and 'co2' to create a record
# that is then stored into the database
import sqlite3 as db
import sys

date = sys.argv[1]
co2 = sys.argv[2]

conn = None

# Function that inserts the record into the database
def create_temp_log(conn, log):
	sql = ''' INSERT INTO co2(Date, CO2)
		VALUES(?,?,?);'''
	cur = conn.cursor()
	cur.execute(sql, log)
	conn.commit()
	print("Log inserted successfully into co2 table")
	return cur.lastrowid

# Setup connection to database
try:
	conn = db.connect('co2.db')
	print("Connected to database")
	log = (date, co2)
	log_id = create_temp_log(conn, log)

except db.Error, e:
	print "Error %s:" %e.args[0]
	sys.exit(1)

finally:
	if conn:
		conn.close()
		print("Database connection closed")
