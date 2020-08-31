from mysql.connector import Error
from database.connector import connect
from database.querys import select, update
from analise import analise

if __name__== '__main__':
	con = connect()

	if con:
		result = select(1, con)

		for line in result:
			result = analise(line[1])
			print(result)
			update(line[0], result, con)