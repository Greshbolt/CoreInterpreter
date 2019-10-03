from Tokenizer import TokList
from Decl import Decl
class DeclSeq:
    def __init__(self):
        self.decl = None
        self.decl_seq = None
    def parse(self):
        self.decl = Decl()
        self.decl.parse()
        if TokList.checkTok('BEGIN'):
            return
        self.decl_seq = DeclSeq()
        self.decl_seq.parse()
    def print(self):
        self.decl.print()
        if self.decl_seq is not None:
            self.decl_seq.print()
    def exec(self):
        pass