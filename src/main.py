import time
from datetime import datetime
from mysql.connector import Error
from database.connector import connect
from database.querys import select, update
from analise import analise
from log import Log

if __name__== '__main__':
	con = connect()
	tempoExecucao = []
	total = 0
	log = Log()
	qtdeItens = 100
	if con:
		log.saveLog('Registro da analise de '+ str(qtdeItens) +' Tweets\n')
		result = select(qtdeItens, con)
		for line in result:
			inicio = time.time()
			result = analise(line[1])
			final = time.time()
			update(line[0], result, con)
			tempoExecucao.append('id: '+ str(line[0]) +' - ' + str(final - inicio) + '\n')
			total += final - inicio
		tempoExecucao.append("Tempo total de execucao: " + str(total))	
		log.saveLog(tempoExecucao)
		log.closeFile()



