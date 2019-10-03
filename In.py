from Tokenizer import TokList
from IdList import IdList
class In:
    def __init__(self):
        self.idList = None
    def parse(self):
        TokList.match('INPUT', 'input')
        self.idList = IdList()
        self.idList.parse()
        TokList.match('SEMICOLON', 'input')
    def print(self):
        TokList.printIndent()
        print('input ', end='')
        self.idList.print()
        print(';')
    def exec(self):
        self.idList.setIdValues()