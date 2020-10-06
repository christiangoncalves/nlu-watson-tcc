import time
from datetime import datetime
from mysql.connector import Error
from database.connector import connect
from database.querys import select, update
from analise import analise
from log import Log

if __name__== '__main__':
	con = connect()
	totalTime = []
	total = 0
	log = Log()
	
	if con:
		result = select(1, con)
		for line in result:
			inicio = time.time()
			result = analise(line[1])
			final = time.time()
			print(result)
			update(line[0], result, con)
			totalTime.append(str(final - inicio) + '\n')
			total += final - inicio
		totalTime.append("Tempo total de execucao: " + str(total))	
		log.saveLog('qtde itens do select: 1\n')
		log.saveLog(totalTime)
		log.closeFile()


