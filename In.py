from Tokenizer import TokList
from IdList import IdList
class In:
    def __init__(self):
        self.idList = None
    #Simple parsing for input statement
    def parse(self):
        TokList.match('INPUT', 'input')
        self.idList = IdList()
        self.idList.parse()
        TokList.match('SEMICOLON', 'input')
    #Simple printing
    def print(self):
        TokList.printIndent()
        print('input ', end='')
        self.idList.print()
        print(';')
    #Execution that sets values in the idList based on the data file
    def exec(self):
        self.idList.setIdValues(0)