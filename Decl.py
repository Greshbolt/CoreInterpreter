from Tokenizer import TokList
from IdList import IdList
class Decl:
    def __init__(self):
        self.id_list = None
    #Simple parsing
    def parse(self):
        TokList.match('INT', "decl")
        self.id_list = IdList()
        self.id_list.parse()
        TokList.match('SEMICOLON', "decl")
    #Simple printing
    def print(self):
        #This form of print is used to not print to a new line after executed
        print('int ', end='')
        self.id_list.print()
    def exec(self):
        #Used to initialize the Ids for future use
        self.id_list.setIdValues(1)