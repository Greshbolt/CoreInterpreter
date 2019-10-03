from Tokenizer import TokList
from Stmt import Stmt
class StmtSeq:
    def __init__(self):
        self.stmt = None
        self.stmt_seq = None
    def parse(self):
        self.stmt = Stmt()
        self.stmt.parse()
        if TokList.checkTok('END'):
            return
        self.stmt_seq = StmtSeq()
        self.stmt_seq.parse()
    def print(self):
        self.stmt.print()
        if self.stmt_seq is not None:
           self.stmt_seq.print()
    def exec(self):
        pass 