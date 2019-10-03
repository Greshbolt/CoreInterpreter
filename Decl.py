from Tokenizer import TokList
from IdList import IdList
class Decl:
    def __init__(self):
        self.id_list = None
    def parse(self):
        TokList.match('INT', "decl")
        self.id_list = IdList()
        self.id_list.parse()
        TokList.match('SEMICOLON', "decl")
    def print(self):
        print('int ', end='')
        self.id_list.print()
    def exec(self):
        pass