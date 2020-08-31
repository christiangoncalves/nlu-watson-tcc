import sys, os
import mysql.connector
from mysql.connector import Error
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import settings as env

def connect():
	'''
	PT-BR: 
	Conecta no banco de dados e retorna a conexão

	EN: 
	Connect to the database and return the connection
	'''
	try:
		con = mysql.connector.connect(host = env.HOST, database=env.DATABASE, user=env.USER, password = env.PASSWORD, charset = env.CHARSET)

		if con.is_connected():
			return con

		return 0

	except Error as e:
		print(e)
		return 0