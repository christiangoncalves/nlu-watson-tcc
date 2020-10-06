from datetime import datetime
class Log():

    def __init__ (self ):
        self.dthr = datetime.now().strftime("%d_%m_%Y_%H_%M")
        self.name ='logs/Log_' + self.dthr +'.txt'
        self.file = open(self.name, 'w+')
        self.file.write('log gerado em: '+self.dthr+'\n')

    def reOpenFile(self):
        self.file = open(self.name, 'r')

    def saveLog(self, lines):
        self.file.writelines(lines)

    def closeFile(self):
        self.file.close()