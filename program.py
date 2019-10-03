from Tokenizer import TokList
from DeclSeq import DeclSeq
from StmtSeq import StmtSeq
class Program:
    def __init__(self):
        self.decl_seq = None
        self.stmt_seq = None
    def parse(self):
        TokList.match("PROGRAM")
        self.decl_seq = DeclSeq()
        self.decl_seq.parse()
        TokList.match("BEGIN")
        self.stmt_seq = StmtSeq()
        self.stmt_seq.parse()
        TokList.match("END")
        TokList.match("EOF")
    def print(self):
        print("program\n")
        self.decl_seq.print()
        print("begin\n")
        self.stmt_seq.print()
        print("end\n")


