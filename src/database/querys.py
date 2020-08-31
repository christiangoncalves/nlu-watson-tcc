import sys
from mysql.connector import Error

def select(qtd, con):
	try:
		cursor = con.cursor()
		query = "SELECT id, tweet from covid limit " + str(qtd)
		cursor.execute(query)
		
		return cursor.fetchall()

	except Error as e:
		print(e)

def update(id, analise, con):
	try:		
		cursor = con.cursor()
		query = "update covid set json_analysis = '"+ str(analise) + "' where id = " + str(id)
		cursor.execute(query)
		
		con.commit()

	except Error as e:
		print(e)