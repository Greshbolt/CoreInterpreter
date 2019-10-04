from Tokenizer import TokList
from Decl import Decl
class DeclSeq:
    def __init__(self):
        self.decl = None
        self.decl_seq = None
    #Simple parsing
    def parse(self):
        self.decl = Decl()
        self.decl.parse()
        #Checks if the decl_seq is at an end
        if TokList.checkTok('BEGIN'):
            return
        self.decl_seq = DeclSeq()
        self.decl_seq.parse()
    #Simple printing
    def print(self):
        TokList.printIndent()
        self.decl.print()
        print(';')
        if self.decl_seq is not None:
            self.decl_seq.print()
    #Simple executing
    def exec(self):
        self.decl.exec()
        if self.decl_seq is not None:
            self.decl_seq.exec()