from mysql.connector import Error
from database.connector import connect
from database.querys import select, update

if __name__== '__main__':
	con = connect()

	result = select(10, con)

	for x in result:
		update(x[0],'salve', con)