from Tokenizer import TokList
from Stmt import Stmt
class StmtSeq:
    def __init__(self):
        self.stmt = None
        self.stmt_seq = None
    #Parses and checks for when it will encounter and end keyword to return
    def parse(self):
        self.stmt = Stmt()
        self.stmt.parse()
        if TokList.checkTok('END') or TokList.checkTok('ELSE') or TokList.checkTok('ENDIF') or TokList.checkTok('ENDWHILE'):
            return
        self.stmt_seq = StmtSeq()
        self.stmt_seq.parse()
    #Simple printing
    def print(self):
        self.stmt.print()
        if self.stmt_seq is not None:
           self.stmt_seq.print()
    #Simple executing
    def exec(self):
        self.stmt.exec()
        if self.stmt_seq is not None:
            self.stmt_seq.exec()